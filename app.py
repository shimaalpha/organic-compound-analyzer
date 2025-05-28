import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    return df

data = load_data()

st.title("🔬 Chemical Test Analyzer")
st.markdown("### Functional Group Identification")

state = st.radio("What is the physical state of the compound?", ["solid", "Liquid"])
bp_or_mp = st.text_input("Boiling or Melting point (°C):", "")

tests = {
    'soot': "Does the compound produce black smoke?",
    'Sulfur': "Does the compound contain sulfur?",
    'Nitrogen': "Does the compound contain nitrogen?",
    'Isocyanate': "Is there an isocyanate group?",
    'Chlorine': "Presence of chlorine?",
    'Bromine': "Presence of bromine?",
    'Iodine': "Presence of iodine?",
    'Alcohol (CAN test)': "Is CAN test for alcohol positive?",
    'Alcohol/Aldehyde (Jones)': "Is Jones test for alcohol/aldehyde positive?",
    'Tertiary Alcohol (Lucas)': "Is Lucas test positive?",
    'Carbonyl Group': "Is a carbonyl group identified?",
    'Carboxylic Acid': "Is a carboxylic acid present?",
    'Phenol': "Is phenol present?",
    'Carbohydrate': "Is it a carbohydrate?",
    'Unsaturation (C=C or C≡C)': "Is unsaturation observed?",
    'Anhydride': "Is an anhydride group present?"
}

user_inputs = {
    'State': state,
    'bp or mp': bp_or_mp
}

for key, question in tests.items():
    user_inputs[key] = st.selectbox(question, ["", "Yes", "No"], index=0)

if st.button("🔍 Search"):
    filtered = data.copy()
    for key, value in user_inputs.items():
        if value and value != "":
            filtered = filtered[filtered[key].astype(str).str.strip().str.lower() == value.lower()]

    if not filtered.empty:
        st.success("✅ The following compounds match your inputs:")
        st.dataframe(filtered[['name', 'State', 'bp or mp']])
    else:
        st.warning("❌ No matching compounds found.")

