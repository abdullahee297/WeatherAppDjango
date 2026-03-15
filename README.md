🌦️ Django Weather Forecast App

A simple Weather Forecast Web Application built with Django that fetches real-time weather data using the OpenWeatherMap API.
Users can search for any city and instantly view the current weather conditions.

🚀 Features

🌍 Search weather by city name

🌡️ Displays current temperature

☁️ Shows weather description

🎨 Displays weather icons

📅 Shows the current date

⚠️ Error handling for invalid city names

⚡ API integration using Python requests

🛠️ Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

API: OpenWeatherMap API

Library: Requests

📂 Project Structure
weather_project/
│
├── weatherapp/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── weatherapp/
│   │       └── index.html
│
├── manage.py
└── requirements.txt
⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/yourusername/django-weather-app.git

2️⃣ Navigate into the project

cd django-weather-app

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the server

python manage.py runserver

5️⃣ Open your browser and go to:

http://127.0.0.1:8000
🔑 API Configuration

This project uses the OpenWeatherMap API.

Create a free API key at
https://openweathermap.org/api

Replace the API key in views.py:

"appid": "YOUR_API_KEY"
📸 Demo

Add a screenshot of your app here.

Example:

![Weather App Screenshot](screenshot.png)
💡 What I Learned

How to integrate external APIs in Django

Handling JSON responses from APIs

Passing dynamic data from views to templates

Implementing basic error handling

Building a real-world backend project

🔗 Author

Muhammad Abdullah

GitHub: https://github.com/yourusername

LinkedIn: (add your LinkedIn profile here)

⭐ If you like this project, feel free to star the repository!
