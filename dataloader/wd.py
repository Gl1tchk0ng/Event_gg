from .forms import EventSearchForm
from .dfilter import filter_events_by_date_range
def mapping_date_and_getting_coordinates():
    date = EventSearchForm.cleaned_data['date']
    events_within_range = filter_events_by_date_range(date)
    coordinates = [(event.latitude, event.longitude) for event in events_within_range]
    return coordinates