
import streamlit as st

st.set_page_config(page_title="Build Your Profile", layout="wide")

# Custom CSS to constrain field widths
st.markdown("""
    <style>
    .stTextInput [data-baseweb="input"] {
        max-width: 400px; /* Adjust based on estimated character length */
    }
    .stNumberInput [data-baseweb="input"] {
        max-width: 200px; /* Adjust based on numeric field width */
    }
    .stSelectbox [data-baseweb="select"] {
        max-width: 300px; /* Adjust based on longest dropdown option */
    }
    .short-select [data-baseweb="select"] {
        max-width: 150px; /* Shorter select boxes for Yes/No and # of units */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Build Your Profile")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🧍 Personal Details")
    first_name = st.text_input("First Name", max_chars=50)
    last_name = st.text_input("Last Name", max_chars=50)

    st.markdown("### 🏡 Subject Property")
    property_address = st.text_input("Property Address", max_chars=75)
    estimated_value = st.number_input("Estimated Value ($)", min_value=0.0, max_value=9999999999.00, step=1000.0)
    occupancy_type = st.selectbox("Intended Occupancy", ["Owner-Occupied", "Second Home", "Investment"])

    flood_col1, flood_col2 = st.columns([2, 1])
    with flood_col1:
        st.write("Flood Zone")
    with flood_col2:
        flood_zone = st.selectbox("", ["Yes", "No"], key="flood_zone")

    units_col1, units_col2 = st.columns([2, 1])
    with units_col1:
        st.write("# of units")
    with units_col2:
        num_units = st.selectbox("", [1, 2, 3, 4], key="num_units")

with col2:
    st.markdown("### 💵 Financial Information")
    cash_available = st.number_input("Cash Available to Close ($)", min_value=0.0, max_value=9999999999.00, step=1000.0)
    qualifying_income = st.number_input("Qualifying Income ($/year)", min_value=0.0, max_value=9999999999.00, step=1000.0)
    monthly_debts = st.number_input("Included Monthly Debts ($)", min_value=0.0, max_value=9999999999.00, step=100.0)

    st.markdown("### 🏘️ Accessory Unit")
    accessory_col1, accessory_col2 = st.columns([2, 1])
    with accessory_col1:
        st.write("Does the property have an accessory unit?")
    with accessory_col2:
        accessory_unit = st.selectbox("", ["No", "Yes"], key="accessory_unit")
    
    if accessory_unit == "Yes":
        separation_col1, separation_col2 = st.columns([2, 1])
        with separation_col1:
            st.write("Interior separation from primary unit?")
        with separation_col2:
            interior_separation = st.selectbox("", ["No", "Yes"], key="interior_separation")

        kitchen_col1, kitchen_col2 = st.columns([2, 1])
        with kitchen_col1:
            st.write("Kitchen with fridge, stove, sink?")
        with kitchen_col2:
            has_kitchen = st.selectbox("", ["No", "Yes"], key="has_kitchen")

        bathroom_col1, bathroom_col2 = st.columns([2, 1])
        with bathroom_col1:
            st.write("Bathroom present?")
        with bathroom_col2:
            has_bathroom = st.selectbox("", ["No", "Yes"], key="has_bathroom")

        if all(ans == "Yes" for ans in [interior_separation, has_kitchen, has_bathroom]) and num_units == 1:
            proposed_rent = st.number_input("Proposed Market Rent for Accessory Unit ($)", min_value=0.0)

st.button("✅ Save Profile")
