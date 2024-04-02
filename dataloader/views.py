from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import addevent, EventSearchForm
from django.views.generic import TemplateView
from .models import Eventdata
from .dfilter import filter_events_by_date_range , dist_cal
def add_event(request):
  if request.method == 'POST':
    form = addevent(request.POST)
    if form.is_valid():
      form.save()
      message = "Event added successfully!"
      return redirect(reverse('event_list')) 
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
            events = filter_events_by_date_range(date)
            #coordinates = get_event_co(date)
            distance = dist_cal(user_lat, user_lon ,date)
            context = {
                'events': events[:5],
                #'coordinates': coordinates[:5],
                'distance': distance[:5],
            }
            return render(request, 'search_events.html', context)

    else:
        form = EventSearchForm() 

    return render(request, 'search_events.html', {'form': form})




