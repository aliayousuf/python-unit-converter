
import streamlit as st

 #Custom CSS for styling
st.set_page_config(page_title="Unit Converter", layout="centered")
st.markdown(
     """
     <style>
    .stApp {
         background: linear-gradient(135deg, #1f4037, #99f2c8);
         color: white;
         font-family: 'Arial', sans-serif;
     }
    
     .stSelectbox, .stNumberInput {
         border-radius: 10px;
         padding: 8px;
     }
.result-box {
        background: #99f2c8;
        color:black;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
    }
     </style>
     """,
     unsafe_allow_html=True
 )
# Conversion dictionary
conversion_factors = {
    "Area": {
        "Square Meter": 1,
        "Square Kilometer": 1e-6,
        "Square Centimeter": 10000,
        "Square Millimeter": 1e6,
        "Square Micrometer": 1e12,
        "Hectare": 1e-4,
        "Square Mile": 3.861e-7,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639,
        "Square Inch": 1550,
        "Acre": 0.000247105
    },
    "Data Transfer Rate": {
         "Bits per second": 1.0,
        "Kilobits per second": 1000.0,
        "Megabits per second": 1000000.0,
        "Gigabits per second": 1000000000.0
    },
    "Digital Storage": {
        "Bit": 1.0,
        "Byte": 8.0,
        "Kilobyte": 8000.0,
        "Megabyte": 8000000.0,
        "Gigabyte": 8000000000.0,
        "Terabyte": 8000000000000.0
    },
    "Energy": {
         "Joule": 1.0,
        "Kilojoule": 1000.0,
        "Calorie": 4.184,
        "Kilocalorie": 4184.0,
        "Kilowatt-hour": 3600000.0,
        "Electronvolt": 1.60218e-19
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 0.001,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9
    },
    "Fuel Economy": {
         "Miles per gallon (US)": 1.0,
        "Miles per gallon (UK)": 1.20095,
        "Kilometers per liter": 0.425144,
        "Liters per 100km": 235.215
    },
    "Length": {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 0.000001,
        "Nanometer": 0.000000001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852.0,
        
         },
    "Pressure": {
         "Pascal": 1.0,
        "Kilopascal": 1000.0,
        "Bar": 100000.0,
        "Atmosphere": 101325.0,
        "PSI": 6894.76,
        "Torr": 133.322
    },
     "Plane Angle": {
         "Degree": 1.0,
        "Arcsecond": 1 / 3600,
        "Gradian": 0.9,
        "Milliradian": 0.0572958,
        "Minute of arc": 1 / 60,
        "Radian": 57.2958
    },
    "Speed": {
         "Meters per second": 1.0,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knots": 0.514444,
        "Feet per second": 0.3048
    },

    "Temperature": {
         "Celsius": 1.0,
        "Fahrenheit": 33.8,
        "Kelvin": 274.15},
   "Time": {
         "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
        "Week": 604800.0,
        "Month": 2629746.0,
        "Year": 31556952.0
    },
     "Volume": {
         "Liter": 1.0,
        "Milliliter": 0.001,
        "Cubic meter": 1000.0,
        "Cubic centimeter": 0.001,
        "Gallon (US)": 3.78541,
        "Gallon (UK)": 4.54609,
        "Quart": 0.946353,
        "Pint": 0.473176
    },
    "Weight (Mass)": {
         "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Microgram": 0.000000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Stone": 6.35029,
        "Ton (metric)": 1000.0
    },
 }


 # Function to handle temperature conversion separately
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return None



# Streamlit UI
st.title("⚡ Unit Converter")

# Select conversion type
conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))

# Get units based on selected type
if conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
else:
    units = list(conversion_factors[conversion_type].keys())

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("🔄 From Unit", units, index=0)

with col2:
    to_unit = st.selectbox("🔁 To Unit", units, index=0)

# User input
value = st.number_input("Enter Value", value=1.0, step=0.1, format="%f")

# Perform conversion dynamically
if conversion_type == "Temperature":
    converted_value = convert_temperature(value, from_unit, to_unit)
else:
    converted_value = value * (conversion_factors[conversion_type][from_unit] / conversion_factors[conversion_type][to_unit])

# Format input and output
formatted_input = f"{int(value)}" if value % 1 == 0 else f"{value:.6f}".rstrip("0").rstrip(".")
formatted_output = f"{int(converted_value)}" if converted_value % 1 == 0 else f"{converted_value:.6f}".rstrip("0").rstrip(".")


# Show result dynamically
st.markdown(f"<div class='result-box'>{formatted_input} {from_unit} = {formatted_output} {to_unit}</div>", unsafe_allow_html=True)







