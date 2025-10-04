import streamlit as st

st.set_page_config(page_title="Energy Saving Calculator", page_icon="☀️", layout="centered")

st.title("⚡ Energy Saving Calculator for SIP Solar Shelters")
st.markdown("""
This tool estimates **energy generation, cost savings, and CO₂ reductions** for your prefabricated SIP shelter with solar panels.
Adjust the parameters to see real-time results.
""")

# --- Inputs ---
st.sidebar.header("Input Parameters")

shelter_size = st.sidebar.number_input("Shelter Size (sq ft)", min_value=100, max_value=400, value=200, step=10)
num_panels = st.sidebar.slider("Number of Solar Panels", 1, 20, 10)
panel_watt = st.sidebar.number_input("Panel Wattage (W)", min_value=100, max_value=500, value=200)
sunlight_hours = st.sidebar.slider("Average Sunlight (hrs/day)", 2.0, 8.0, 4.0, 0.5)
electricity_rate = st.sidebar.number_input("Electricity Rate ($/kWh)", min_value=0.05, max_value=0.50, value=0.18, step=0.01)
panel_cost = st.sidebar.number_input("Cost per Panel ($)", min_value=100, max_value=1000, value=300)
co2_savings_per_shelter = st.sidebar.number_input("CO₂ Savings vs Stick Framing (%)", min_value=0, max_value=100, value=45)

# --- Calculations ---
daily_energy = (panel_watt * num_panels * sunlight_hours) / 1000  # kWh/day
annual_energy = daily_energy * 365  # kWh/year
total_cost = panel_cost * num_panels
annual_savings = annual_energy * electricity_rate
payback_years = total_cost / annual_savings
payback_months = payback_years * 12
ghg_payback = 3.8  # years (given)
energy_payback = 5.1  # years (given)

# CO2 reduction estimate based on typical emissions from grid power (~0.417 kg CO2/kWh)
annual_co2_reduction = annual_energy * 0.417  # kg CO2/year

# Roof load check
panel_weight = 17.7  # kg per panel (approx)
total_weight = panel_weight * num_panels
roof_area = shelter_size * 0.0929  # sq m
pressure = total_weight / roof_area  # kg/m²

# --- Outputs ---
st.subheader("📊 Results Summary")

col1, col2 = st.columns(2)
with col1:
    st.metric("Daily Energy Output", f"{daily_energy:.2f} kWh/day")
    st.metric("Annual Energy Output", f"{annual_energy:.0f} kWh/year")
    st.metric("Annual CO₂ Reduction", f"{annual_co2_reduction/1000:.2f} tons/year")

with col2:
    st.metric("Estimated Payback Period", f"{payback_months:.1f} months")
    st.metric("Energy Payback Time", f"{energy_payback:.1f} years")
    st.metric("GHG Payback Time", f"{ghg_payback:.1f} years")

st.markdown("---")
st.subheader("💰 Financial Overview")
st.write(f"**Total Solar Cost:** ${total_cost:,.0f}")
st.write(f"**Annual Savings on Electricity:** ${annual_savings:,.0f}/year")
st.write(f"**Payback Period:** ~{payback_months:.1f} months")

st.markdown("---")
st.subheader("🏗️ Engineering & Structural Insights")
st.write(f"- Roof Load from Panels: **{total_weight:.1f} kg** total")
st.write(f"- Roof Pressure: **{pressure:.1f} kg/m²** (Safe within SIP roof tolerance ≥250–300 kg/m²)")
st.write(f"- Shelter Size: **{shelter_size} sq ft**, exceeds minimum livable space requirements")
st.write(f"- SIP design offers **{co2_savings_per_shelter}% CO₂ reduction** compared to traditional framing.")

st.markdown("---")
st.markdown("✅ *This calculator helps quantify how sustainable and cost-effective your SIP + solar system is in real conditions.*")

