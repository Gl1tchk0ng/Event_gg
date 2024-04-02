from datetime import timedelta
from .models import Eventdata
import requests
from django.http import JsonResponse
def filter_events_by_date_range(date):
    end_date = date + timedelta(days=14)
    events_within_range = Eventdata.objects.filter(date__range=(date, end_date))
    return events_within_range

def get_event_co(date):
  events_within_range = filter_events_by_date_range(date)
  return [(event.latitude, event.longitude) for event in events_within_range]


def dist_cal(user_lat, user_lon, date):
  events = get_event_co(date)
  distance_api_url = "https://gg-backend-assignment.azurewebsites.net/api/Distance?code=IAKvV2EvJa6Z6dEIUqqd7yGAu7IZ8gaH-a0QO6btjRc1AzFu8Y3IcQ=="
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

#def get_weather_data(user_lat, user_lon, date):
  Eve
  weather_api_url = "https://gg-backend-assignment.azurewebsites.net/api/Weather?code=KfQnTWHJbg1giyB_Q9Ih3Xu3L9QOBDTuU5zwqVikZepCAzFut3rqsg=="
  url = f"{weather_api_url}&city={city}&date={date}"
  try:
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data for {city} on {date}: {e}")
    return None

