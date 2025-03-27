
import streamlit as st

st.set_page_config(page_title="Build Your Profile", layout="wide")

# CSS to adjust layout and input box sizes
st.markdown(
    '''
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        input[type="text"], input[type="number"] {
            height: 30px;
        }
        .stTextInput > div > div > input {
            font-size: 14px;
        }
        .stNumberInput > div > div {
            width: 120px !important;
        }
        .stSelectbox > div {
            width: 150px !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

st.title("📄 Build Your Profile")

# Layout
col1, col2, col3, col4 = st.columns([1.5, 1.5, 1.2, 1.2])

with col1:
    st.subheader("👤 Personal Details")
    first_name = st.text_input("First Name", max_chars=50)
    last_name = st.text_input("Last Name", max_chars=50)

with col2:
    st.subheader("💵 Financial Info")
    cash_available = st.number_input("Cash Available ($)", min_value=0.0, max_value=9999999999.0, step=1000.0)
    qualifying_income = st.number_input("Qualifying Income ($/year)", min_value=0.0, max_value=9999999999.0, step=1000.0)
    monthly_debts = st.number_input("Monthly Debts ($)", min_value=0.0, max_value=9999999999.0, step=100.0)

with col3:
    st.subheader("🏠 Property Info")
    address = st.text_input("Property Address", max_chars=75)
    estimated_value = st.number_input("Estimated Value ($)", min_value=0.0, max_value=9999999999.0, step=1000.0)
    occupancy = st.selectbox("Intended Occupancy", ["Owner-Occupied", "Second Home", "Investment"])
    flood_zone = st.selectbox("Flood Zone", ["Yes", "No"])
    units = st.selectbox("Number of Units", [1, 2, 3, 4])

with col4:
    st.subheader("🏡 Accessory Unit")
    has_ad
    
