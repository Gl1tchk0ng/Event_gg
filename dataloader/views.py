from django.shortcuts import render, redirect
from .forms import addevent
from django.views.generic import TemplateView
from .models import Eventdata
def add_event(request):
  if request.method == 'POST':
    form = addevent(request.POST)
    if form.is_valid():
      form.save()
      message = "Event added successfully!"
      return redirect('success_url')  # Replace 'success_url' with actual redirect URL
  else:
    form = addevent()
  return render(request, 'addevent.html', {'form': form})

class EventListView(TemplateView):
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Eventdata.objects.all()
        return context
