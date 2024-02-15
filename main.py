import streamlit as zx

zx.title("Weather Forecast for the next Days")

city = zx.text_input("City: ")
day = zx.slider("Number of days for the forecast: ", min_value=1, max_value=5,
                help="Select the number of days you want to see forecast of")
options = zx.selectbox("Select the type of data to view", ("Temperature", "Sky view"))
zx.subheader(f"{options} for the next {day} days at {city}: ")
