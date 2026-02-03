from django.shortcuts import render
import requests
import datetime

def home(request):

    city = request.POST.get('city', 'kalam')

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "3318668cd21f3cdd15ee121cd3f89c1c",
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # If city is invalid or API fails
    if response.status_code != 200:
        return render(request, "weatherapp/index.html", {
            "error": data.get("message", "Something went wrong"),
            "city": city
        })

    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    temp = data["main"]["temp"]
    day = datetime.date.today()

    context = {
        "description": description,
        "icon": icon,
        "temp": temp,
        "day": day,
        "city": city,
    }

    return render(request, "weatherapp/index.html", context)
