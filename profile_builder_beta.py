
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
    flood_zone = st.selectbox("Flood Zone", ["Yes", "No"], key="flood_zone", css_classes="short-select")
    num_units = st.selectbox("# of units", [1, 2, 3, 4], key="num_units", css_classes="short-select")

with col2:
    st.markdown("### 💵 Financial Information")
    cash_available = st.number_input("Cash Available to Close ($)", min_value=0.0, max_value=9999999999.00, step=1000.0)
    qualifying_income = st.number_input("Qualifying Income ($/year)", min_value=0.0, max_value=9999999999.00, step=1000.0)
    monthly_debts = st.number_input("Included Monthly Debts ($)", min_value=0.0, max_value=9999999999.00, step=100.0)

    st.markdown("### 🏘️ Accessory Unit")
    accessory_unit = st.selectbox("Does the property have an accessory unit?", ["No", "Yes"], key="accessory_unit", css_classes="short-select")
    if accessory_unit == "Yes":
        interior_separation = st.selectbox("Interior separation from primary unit?", ["No", "Yes"], key="interior_separation", css_classes="short-select")
        has_kitchen = st.selectbox("Kitchen with fridge, stove, sink?", ["No", "Yes"], key="has_kitchen", css_classes="short-select")
        has_bathroom = st.selectbox("Bathroom present?", ["No", "Yes"], key="has_bathroom", css_classes="short-select")
        if all(ans == "Yes" for ans in [interior_separation, has_kitchen, has_bathroom]) and num_units == 1:
            proposed_rent = st.number_input("Proposed Market Rent for Accessory Unit ($)", min_value=0.0)

st.button("✅ Save Profile")
