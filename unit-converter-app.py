import streamlit as st
import base64
import os

st.set_page_config(
    page_title="UniScale ⚖️📏",
    page_icon="📏",
    layout="centered"
)

# Function to Load CSS with Error Handling
def load_css(css_file):
    if os.path.exists(css_file):  # Check if the file exists
        with open(css_file, "r") as f:
            css_content = f"<style>{f.read()}</style>"
            st.markdown(css_content, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ CSS file '{css_file}' not found! Using default styles.")

# Call the function to load CSS
load_css("styles.css")

# Title and Description with Animations
st.markdown("<h1 class='title'> Unit Converter </h1>", unsafe_allow_html=True)
st.markdown("### <p class='description'>UniScale  – Fast & easy unit conversion for length, weight, time, height and temperature! 🚀</p>", unsafe_allow_html=True)

st.sidebar.title(" Dashboard Unit Converter")
# Unit Category Selection
category = st.sidebar.selectbox("⚖️ Select a Conversion", [
    "📏 Length", "⚖️ Weight", "🕰️ Time", "📐 Height", "🌡️ Temperature"
])

# **Show Selected Category as Heading**
st.markdown(f"<h2 class='category-heading'>{category} Conversion</h2>", unsafe_allow_html=True)

# Conversion Logic
def convert_units(category, value, unit):
    if category == "📏 Length":
       return value * 0.621371 if unit == "Kilometers to Miles" else value / 0.621371
    elif category == "⚖️ Weight":
        return value * 2.20462 if unit == "Kilograms to Pounds" else value / 2.20462
    elif category == "🕰️ Time":
        conversions = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24
        }
        return conversions.get(unit, value)
    elif category == "📐 Height":
        return value * 3.28084 if unit == "Meters to Feet" else value / 3.28084 
    elif category == "🌡️ Temperature":
        return (value * 9/5) + 32 if unit == "Celsius to Fahrenheit" else (value - 32) * 5/9


if category == "📏 Length":
    unit = st.selectbox("📏 Select a Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "⚖️ Weight":
    unit = st.selectbox("⚖️ Select a Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "🕰️ Time":
    unit = st.selectbox("🕰️ Select a Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
elif category == "📐 Height":
    unit = st.selectbox("📐 Select a Conversion", ["Meters to Feet", "Feet to Meters"])
elif category == "🌡️ Temperature":
    unit = st.selectbox("🌡️ Select a Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])


value = st.number_input("🧮 Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"{value} {unit.split(' to ')[0]} is equal to {result:.2f} {unit.split(' to ')[1]}")

st.markdown("""
    <div style="text-align: center; padding: 10px; font-size: 18px; color: white;">
        © 2025 | Developed by <b style='color:#87CEEB;font-size:20px;'>Syed Faisal Mehmood</b> ⚖️
        <br>
        <a href="ww.linkedin.com" target="_blank" style="color: #87CEEB; text-decoration: none;">
            🔗 Connect on LinkedIn
        </a>
    </div>
""", unsafe_allow_html=True)

