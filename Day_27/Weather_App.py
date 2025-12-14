import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌦️", layout="centered")
st.title("🌦️ Weather App")
st.write("Real-time weather with OpenWeatherMap API")

# Try secrets first (secure way)
try:
    API_KEY = st.secrets["API_KEY"]
except:
    st.error("No API key in secrets.toml! Add it there for security.")
    st.stop()

# Unit toggle
units = st.radio("Units:", ("Metric (°C, m/s)", "Imperial (°F, mph)"), horizontal=True)
unit_param = "metric" if "Metric" in units else "imperial"
temp_unit = "°C" if unit_param == "metric" else "°F"

city = st.text_input("City Name:", placeholder="e.g., Lahore")

if st.button("Get Weather"):
    if not city:
        st.error("Enter a city!")
    else:
        with st.spinner("Loading..."):
            params = {"q": city.title(), "appid": API_KEY, "units": unit_param}
            response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
            data = response.json()

            if response.status_code != 200:
                st.error(f"Error: {data.get('message', 'Try again')}")
            else:
                icon_url = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png"
                col1, col2 = st.columns([1, 2])
                with col1: st.image(icon_url, width=150)
                with col2:
                    st.success(f"**{data['name']}, {data['sys']['country']}**")
                    st.subheader(data['weather'][0]['description'].title())

                st.metric("Temperature", f"{data['main']['temp']} {temp_unit}", f"Feels {data['main']['feels_like']} {temp_unit}")
                st.write(f"Humidity: {data['main']['humidity']}% | Wind: {data['wind']['speed']} {'m/s' if unit_param=='metric' else 'mph'}")