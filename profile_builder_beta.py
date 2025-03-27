
import streamlit as st

st.set_page_config(page_title="Build Your Profile", layout="wide")

st.markdown("""
    <style>
    input[type="text"] {
        width: 400px;
    }
    .stNumberInput input {
        width: 250px;
    }
    .stSelectbox div[data-baseweb="select"] {
        width: 250px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Build Your Profile")

# Consolidated layout
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown("### 🧍 Personal")
        first_name = st.text_input("First Name", max_chars=50)
        last_name = st.text_input("Last Name", max_chars=50)

        st.markdown("### 🏡 Property")
        property_address = st.text_input("Address", max_chars=75)
        estimated_value = st.number_input("Estimated Value ($)", min_value=0.0, max_value=9999999999.00, step=1000.0)

    with col2:
        occupancy_type = st.selectbox("Occupancy", ["Owner-Occupied", "Second Home", "Investment"])
        flood_zone = st.selectbox("Flood Zone", ["No", "Yes"])
        num_units = st.selectbox("Units", [1, 2, 3, 4])

        st.markdown("### 🏘️ Accessory Unit")
        accessory_unit = st.selectbox("Accessory Unit?", ["No", "Yes"])
        if accessory_unit == "Yes":
            interior_separation = st.selectbox("Interior Separation?", ["No", "Yes"])
            has_kitchen = st.selectbox("Full Kitchen?", ["No", "Yes"])
            has_bathroom = st.selectbox("Bathroom?", ["No", "Yes"])
            if all(ans == "Yes" for ans in [interior_separation, has_kitchen, has_bathroom]) and num_units == 1:
                proposed_rent = st.number_input("Accessory Unit Rent ($)", min_value=0.0)

    with col3:
        st.markdown("### 💵 Financials")
        cash_available = st.number_input("Cash to Close ($)", min_value=0.0, max_value=9999999999.00, step=1000.0)
        qualifying_income = st.number_input("Income ($/yr)", min_value=0.0, max_value=9999999999.00, step=1000.0)
        monthly_debts = st.number_input("Monthly Debts ($)", min_value=0.0, max_value=9999999999.00, step=100.0)

st.button("✅ Save Profile")
