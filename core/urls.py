from django.contrib import admin
from django.urls import path
from dataloader import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addevent/',views.add_event),
    path('events/', views.EventListView.as_view(), name='event_list'),
]
