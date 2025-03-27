
import streamlit as st

st.set_page_config(page_title="🏗️ Profile Builder (Beta)", layout="wide")

st.title("📄 Build Your Profile")

with st.form("profile_form"):
    st.subheader("🧍 Personal Details")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    st.subheader("🏠 Subject Property")
    subject_property_address = st.text_input("Property Address")
    estimate_value = st.number_input("Estimated Value ($)", min_value=0.0, format="%.2f")
    intended_occupancy = st.selectbox("Intended Occupancy", ["Owner-Occupied", "Non-Owner", "Vacant", "Other"])
    flood_zone = st.selectbox("Flood Zone", ["Yes", "No"])
    num_units = st.selectbox("# of Units", [1, 2, 3, 4])

    st.subheader("🏘️ Accessory Unit")
    accessory_unit = st.selectbox("Does the property have an accessory unit?", ["Yes", "No"])
    accessory_unit_has_separation = accessory_unit_kitchen_present = accessory_unit_bathroom_present = "No"
    proposed_market_rent = 0.0

    if accessory_unit == "Yes":
        accessory_unit_has_separation = st.selectbox("Interior separation from primary unit?", ["Yes", "No"])
        accessory_unit_kitchen_present = st.selectbox("Kitchen (fridge, cooking appliance, sink)?", ["Yes", "No"])
        accessory_unit_bathroom_present = st.selectbox("Bathroom present?", ["Yes", "No"])

        if (
            num_units == 1 and
            accessory_unit_has_separation == "Yes" and
            accessory_unit_kitchen_present == "Yes" and
            accessory_unit_bathroom_present == "Yes"
        ):
            proposed_market_rent = st.number_input(
                "Proposed Market Rent ($/month)",
                min_value=0.0,
                format="%.2f",
                help="Enter the estimated rent this accessory unit could earn monthly."
            )

    st.subheader("💵 Financial Information")
    cash_available_to_close = st.number_input("Cash Available to Close ($)", min_value=0.0, format="%.2f")
    qualifying_income = st.number_input("Qualifying Income ($/year)", min_value=0.0, format="%.2f")
    included_monthly_debts = st.number_input("Included Monthly Debts ($)", min_value=0.0, format="%.2f")

    submitted = st.form_submit_button("✅ Save Profile")

    if submitted:
        st.session_state.user_profile = {
            "first_name": first_name,
            "last_name": last_name,
            "subject_property_address": subject_property_address,
            "estimate_value": estimate_value,
            "intended_occupancy": intended_occupancy,
            "flood_zone": flood_zone,
            "num_units": num_units,
            "accessory_unit": accessory_unit,
            "accessory_unit_has_separation": accessory_unit_has_separation,
            "accessory_unit_kitchen_present": accessory_unit_kitchen_present,
            "accessory_unit_bathroom_present": accessory_unit_bathroom_present,
            "proposed_market_rent": proposed_market_rent,
            "cash_available_to_close": cash_available_to_close,
            "qualifying_income": qualifying_income,
            "included_monthly_debts": included_monthly_debts
        }
        st.success("Profile saved successfully!")
