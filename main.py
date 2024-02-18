import streamlit as zx
import plotly.express as px
from BackEnd import get_data

zx.title("Weather Forecast for the next Days")

city = zx.text_input("City: ")
day = zx.slider("Number of days for the forecast: ", min_value=1, max_value=5,
                help="Select the number of days you want to see forecast of")
options = zx.selectbox("Select the type of data to view", ("Temperature", "Sky view"))
zx.subheader(f"{options} for the next {day} days at {city}: ")

if city:
    try:
        filtered_data = get_data(city, day)
        if options == "Temperature":
            temp = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            graph = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
            zx.plotly_chart(graph)
        if options == "Sky view":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_view = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_view]
            print(sky_view)
            zx.image(image_path, width=115)
    except KeyError:
        zx.write("That place does not exist. Please enter a correct city!")

