from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("journeys/", views.journeys, name="journeys"),
    path("journeys/<slug:slug>/", views.tour_detail, name="tour_detail"),
    path("save/<slug:slug>/", views.toggle_save, name="toggle_save"),
    path("inquire/", views.inquire, name="inquire"),
    path("transport/", views.transport, name="transport"),
    path("gallery/", views.gallery, name="gallery"),
    path("zanzibar-stories/", views.zanzibar_stories, name="zanzibar_stories"),
    path("plan-your-trip/", views.plan_trip, name="plan_trip"),
]
