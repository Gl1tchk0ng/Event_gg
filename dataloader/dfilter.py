from datetime import timedelta
from .models import Eventdata
import requests
from core import settings
def filter_events_by_date_range(date):
    end_date = date + timedelta(days=14)
    events_within_range = Eventdata.objects.filter(date__range=(date, end_date)).order_by('date')
    return events_within_range

def get_event_co(date):
  events_within_range = filter_events_by_date_range(date)
  return [(event.latitude, event.longitude) for event in events_within_range]


def dist_cal(user_lat, user_lon, date):
  events = get_event_co(date)
  distance_api_url = settings.env('calulatorurl')
  distances = []
  for event in events:
    event_latitude, event_longitude = event
    url = f"{distance_api_url}&latitude1={user_lat}&longitude1={user_lon}&latitude2={event_latitude}&longitude2={event_longitude}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and "distance" in data:
            distances.append(data["distance"])
        else:
            print("Empty distance data received from API.")
    else:
        print(f"Error fetching distance for event: {response.status_code}")
  return distances 
  
import requests

def get_weather_data(date):
    eventcoords = get_event_co(date)
    weather_data = []
    for event_latitude, event_longitude in eventcoords:
        event_data = Eventdata.objects.get(latitude=event_latitude, longitude=event_longitude)
        if event_data:
            city_name = event_data.city_name  
            weather_api_url = settings.env('weatherurl')
            url = f"{weather_api_url}&city={city_name}&date={date}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data and "weather" in data:
                    weather_data.append(data["weather"])
                else:
                    print("Empty weather data received from API.")
            else:
                print(f"Error fetching weather data for {city_name} on {date}: {response.text}")
    return weather_data

