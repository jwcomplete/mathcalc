
import streamlit as st

st.set_page_config(page_title="Build Your Profile", layout="wide")

# Custom CSS for input widths
st.markdown("""
    <style>
    div[data-baseweb="input"] input {
        max-width: 400px;
    }
    .stNumberInput input {
        max-width: 260px;
    }
    div[data-baseweb="select"] {
        max-width: 180px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Build Your Profile")

# --- Personal ---
st.markdown("### 🧍 Personal Details")
first_name = st.text_input("First Name", max_chars=50)
last_name = st.text_input("Last Name", max_chars=50)

# --- Property ---
st.markdown("### 🏡 Subject Property")
property_address = st.text_input("Property Address", max_chars=75)
estimated_value = st.number_input("Estimated Value ($)", min_value=0.0, max_value=9999999999.00, step=1000.0)
occupancy_type = st.selectbox("Intended Occupancy", ["Owner-Occupied", "Second Home", "Investment"])
flood_zone = st.selectbox("Flood Zone", ["Yes", "No"], key="flood_zone")
num_units = st.selectbox("# of Units", [1, 2, 3, 4], key="num_units")

# --- Financial ---
st.markdown("### 💵 Financial Information")
cash_available = st.number_input("Cash Available to Close ($)", min_value=0.0, max_value=9999999999.00, step=1000.0)
qualifying_income = st.number_input("Qualifying Income ($/year)", min_value=0.0, max_value=9999999999.00, step=1000.0)
monthly_debts = st.number_input("Included Monthly Debts ($)", min_value=0.0, max_value=9999999999.00, step=100.0)

# --- Accessory Unit ---
st.markdown("### 🏘️ Accessory Unit")
accessory_unit = st.selectbox("Does the property have an accessory unit?", ["No", "Yes"], key="accessory_unit")

if accessory_unit == "Yes":
    interior_separation = st.selectbox("Interior separation from primary unit?", ["No", "Yes"], key="interior_separation")
    has_kitchen = st.selectbox("Kitchen with fridge, stove, sink?", ["No", "Yes"], key="has_kitchen")
    has_bathroom = st.selectbox("Bathroom present?", ["No", "Yes"], key="has_bathroom")

    if all(ans == "Yes" for ans in [interior_separation, has_kitchen, has_bathroom]) and num_units == 1:
        proposed_rent = st.number_input("Proposed Market Rent for Accessory Unit ($)", min_value=0.0)

# --- Submit ---
st.button("✅ Save Profile")
