# weather-app
# Project Overview

The Weather App is a simple web application that allows users to check the current weather of any city in the world.
It fetches live weather data using the OpenWeatherMap API and displays temperature, weather conditions, and an icon representing the weather.

# Objective

The main goal of this project is to:

Understand how to work with APIs (Application Programming Interfaces).

Learn how to send requests and handle JSON data in Python.

Build a simple, interactive web application using Flask.

# Technologies Used

Python (Flask Framework) – to create the web server.

HTML5 & CSS3 – for designing and styling the frontend.

OpenWeatherMap API – to fetch real-time weather information.

# How It Works

The user enters a city name on the home page.

Flask sends a request to the OpenWeatherMap API with the entered city name.

The API responds with weather data in JSON format.

Flask extracts temperature, weather description, and icon details.

The results are displayed neatly on the webpage.

# Project Structure
weather_app/
│
├── app.py                # Main Python file (Flask app)
│
├── templates/            # HTML templates
│   ├── index.html        # Home page
└── static/               # Static files
    └── style.css         # Styling for the app
