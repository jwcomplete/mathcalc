
import streamlit as st

st.set_page_config(page_title="Build Your Profile", layout="wide")

# Custom CSS for input widths and styling placeholders
st.markdown("""
    <style>
    .element-container:has(.stToggle) { display: flex; align-items: center; gap: 0.5rem; }
    div[data-baseweb="input"] input {
        max-width: 400px;
    }
    .stNumberInput input {
        width: 200px;
    }
    div[data-baseweb="select"] {
        max-width: 180px;
    }
    .stToggle {
        display: flex;
        align-items: center !important;
        margin-top: -0.1rem;
    }
    .stToggle > label {
        margin-top: -8px !important;
    }
    input::placeholder {
        color: lightgray;
    }
    </style>
""", unsafe_allow_html=True)

# JavaScript to handle placeholder behavior
st.markdown("""
    <script>
    const elements = document.querySelectorAll(".stNumberInput input");
    elements.forEach(el => {
        el.onfocus = function() {
            if (this.value === "$0.00") {
                this.value = "";
            }
        };
        el.onblur = function() {
            if (this.value === "") {
                this.value = "$0.00";
            }
        };
    });
    </script>
""", unsafe_allow_html=True)

st.title("📄 Build Your Profile")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🧍 Personal Details")
    first_name = st.text_input("First Name", max_chars=50)
    last_name = st.text_input("Last Name", max_chars=50)

    st.markdown("### 🏡 Subject Property")
    property_address = st.text_input("Property Address", max_chars=75)

    col_val, col_occ, col_flood, col_units = st.columns([2.5, 2, 1.5, 1])
    with col_val:
        st.markdown("**Estimated Value ($)**")
        estimated_value = st.number_input("", min_value=0.0, max_value=9999999999.00, step=1000.0, format="%0.2f", value=0.00)
    with col_occ:
        occupancy_type = st.selectbox("Occupancy", ["Owner-Occupied", "Second Home", "Investment"])
    with col_flood:
        flood_zone = st.selectbox("Flood Zone", ["Yes", "No"], key="flood_zone")
    with col_units:
        num_units = st.selectbox(" # of Units", [1, 2, 3, 4], key="num_units")

    st.markdown("### 🏘️ Accessory Unit")
    col_acc_q, col_acc_a = st.columns([5, 1])
    with col_acc_q:
        st.markdown("**Does the property have an accessory unit?**")
    with col_acc_a:
        accessory_unit = st.checkbox("", value=False, key="accessory_unit")

    if accessory_unit:
        col_sep_q, col_sep_a = st.columns([5, 1])
        with col_sep_q:
            st.markdown("**Interior separation from primary unit?**")
        with col_sep_a:
            interior_separation = st.checkbox("", value=False, key="interior_separation")
        col_kitch_q, col_kitch_a = st.columns([5, 1])
        with col_kitch_q:
            st.markdown("**Kitchen with fridge, stove, sink?**")
        with col_kitch_a:
            has_kitchen = st.checkbox("", value=False, key="has_kitchen")
        col_bath_q, col_bath_a = st.columns([5, 1])
        with col_bath_q:
            st.markdown("**Bathroom present?**")
        with col_bath_a:
            has_bathroom = st.checkbox("", value=False, key="has_bathroom")

        if all([interior_separation, has_kitchen, has_bathroom]) and num_units == 1:
            st.markdown("**Proposed Market Rent for Accessory Unit ($)**")
            proposed_rent = st.number_input("", min_value=0.0, format="%0.2f", value=0.00)

with col2:
    st.markdown("### 💵 Financial Information")
    col_f1, col_f2 = st.columns([1, 1])
    with col_f1:
        st.markdown("**Cash Available to Close ($)**")
        cash_available = st.number_input("", min_value=0.0, max_value=9999999999.00, step=1000.0, format="%0.2f", value=0.00)
        st.markdown("**Included Monthly Debts ($)**")
        monthly_debts = st.number_input("", min_value=0.0, max_value=9999999999.00, step=100.0, format="%0.2f", value=0.00)
    with col_f2:
        st.markdown("**Qualifying Income ($/year)**")
        qualifying_income = st.number_input("", min_value=0.0, max_value=9999999999.00, step=1000.0, format="%0.2f", value=0.00)

st.button("✅ Save Profile")
