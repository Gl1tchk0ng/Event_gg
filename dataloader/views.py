from datetime import timedelta
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import addevent, EventSearchForm
from django.views.generic import TemplateView
from .models import Eventdata
def add_event(request):
  if request.method == 'POST':
    form = addevent(request.POST)
    if form.is_valid():
      form.save()
      message = "Event added successfully!"
      return redirect(reverse('event_list'))  # Replace 'success_url' with actual redirect URL
  else:
    form = addevent()
  return render(request, 'addevent.html', {'form': form})

class EventListView(TemplateView):
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Eventdata.objects.all()
        return context

def search_events(request):
    if request.method == 'POST':
        form = EventSearchForm(request.POST)
        if form.is_valid():
            user_lat = form.cleaned_data['user_latitude']
            user_lon = form.cleaned_data['user_longitude']
            date = form.cleaned_data['date']

            # Calculate the end date (14 days from the specified date)
            end_date = date + timedelta(days=14)

            # Filter events within the date range
            events = Eventdata.objects.filter(date__range=(date, end_date))

            context = {
                'events': events,
            }
            return render(request, 'search_events.html', context)

    else:
        form = EventSearchForm()  # Empty form for initial display

    return render(request, 'search_events.html', {'form': form})