import streamlit as st
from supabase import create_client, Client

st.title("E-Waste Disposal Habits Survey")

st.markdown(
    """
    <style>
    .stMultiSelect span[data-baseweb="tag"] {
        white-space: normal !important;
        height: auto !important;
    }
    div[data-baseweb="select"] > div {
        height: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("E-Waste Disposal Habits Survey")
st.write("Understanding how electronic waste is handled.")

with st.form("comprehensive_ewaste_form"):
    
    st.subheader("1. Location Details")
    area = st.text_input("What is your area, neighborhood, or city?")
    
    st.subheader("2. Demographics")
    age_group = st.selectbox(
        "Select your age group",
        ["Under 18", "18-24", "25-34", "35-44", "45-54", "55 or older"]
    )
    gender = st.selectbox(
        "Gender identity",
        ["Female", "Male", "Non-binary / Prefer not to say"]
    )
    occupation = st.selectbox(
        "Primary occupation",
        ["Student", "Working Professional", "Business Owner / Self-Employed", "Homemaker", "Retired", "Other"]
    )
    income_bracket = st.selectbox(
        "Household income bracket (Optional)",
        ["Prefer not to say", "Low", "Medium", "High"]
    )
    
    st.subheader("3. Device Usage & Habits")
    upgrade_frequency = st.selectbox(
        "How often do you typically upgrade your smartphone or laptop?",
        ["Every 1-2 years", "Every 3-4 years", "Every 5+ years", "Only when it breaks"]
    )
    annual_devices = st.number_input(
        "Roughly how many electronic devices or accessories do you discard or replace per year?",
        min_value=0, max_value=50, value=2
    )
    eco_consciousness = st.slider(
        "How strongly do you consider environmental impact when buying consumer goods?",
        1, 5, 3,
        help="1 = Not at all, 5 = It is my top priority"
    )

    st.subheader("4. Disposal Habits")
    disposal_method = st.multiselect(
        "How do you usually dispose of old or broken electronics?",
        [
            "Throw them in the regular household garbage/bin",
            "Toss them in general recycling bins",
            "Keep/store them indefinitely at home",
            "Sell them or give them away to family/friends",
            "Trade them in when buying new devices",
            "Drop them off at dedicated e-waste collection points or retail drop-boxes"
        ]
    )
    
    st.subheader("5. E-Waste Types")
    common_items = st.multiselect(
        "What type of e-waste do you accumulate the most? (Select all that apply)",
        [
            "Smartphones, tablets, and e-readers (Kindle, etc.)",
            "Laptops, desktop computers, and monitors",
            "Charging cables, adapters, and power banks",
            "Small home appliances (blenders, hair dryers, irons)",
            "Household batteries and small electronics"
        ]
    )
    
    st.subheader("6. Barriers")
    barriers = st.multiselect(
        "What prevents you from recycling your e-waste properly? (Select all that apply)",
        [
            "I don't know where the nearest e-waste drop-off location is.",
            "It is too inconvenient or far away to travel to a collection site.",
            "I am worried about personal data security on old devices.",
            "I didn't know electronics shouldn't go in regular trash.",
            "There are no major barriers; I just haven't gotten around to it."
        ]
    )
    
    st.subheader("7. Awareness")
    awareness = st.slider(
        "How familiar are you with the environmental hazards of improper e-waste disposal?",
        1, 5, 3,
        help="1 = Not aware at all, 5 = Extremely aware"
    )
    
    st.subheader("8. Motivations")
    incentive = st.multiselect(
        "What would motivate you the most to recycle e-waste more frequently? (Select all that apply)",
        [
            "Financial incentives (cashback, store discounts, tax rebates)",
            "Convenient local pickup services right from home",
            "More drop-off bins located in everyday places (grocery stores, malls)",
            "Better awareness campaigns and clear instructions"
        ]
    )
    
    submitted = st.form_submit_button("Submit Survey Response")

    if submitted:
        if not area.strip():
            st.error("Please enter your area or neighborhood before submitting.")
        else:
            try:
                response = supabase.table("e-waste_form-data").insert({
                    "area": area,
                    "age_group": age_group,
                    "gender": gender,
                    "occupation": occupation,
                    "income_bracket": income_bracket,
                    "upgrade_frequency": upgrade_frequency,
                    "annual_devices": annual_devices,
                    "eco_consciousness": eco_consciousness,
                    "disposal_method": ", ".join(disposal_method),
                    "common_items": ", ".join(common_items),
                    "barriers": ", ".join(barriers),
                    "awareness_level": awareness,
                    "preferred_incentive": ", ".join(incentive)
                }).execute()
                
                st.success("Thank you! Your survey response has been recorded securely.")
            except Exception as e:
                st.error(f"Error submitting survey: {e}")