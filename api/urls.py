from django.urls import path
from api.views import (
    SliderListView,
    BrandListView,
    FactListView,
    TeamListView,
    EventListView,
    TeamShortListView,
    MessageCreateView,
    CollectEmailView,
	EventResgistrationView,
	GetInvitationDetailsView
)

urlpatterns = [
    path("sliders", SliderListView.as_view(), name="sliders-list"),
    path("brands", BrandListView.as_view(), name="brand-list"),
    path("facts", FactListView.as_view(), name="fact-list"),
    path("teams", TeamListView.as_view(), name="team-list"),
    path("team-short", TeamShortListView.as_view(), name="team-short"),
    path("message", MessageCreateView.as_view(), name="send-message"),
    path("events", EventListView.as_view(), name="event-list"),
    path("newsletter", CollectEmailView.as_view(), name="newslatter-collect"),
	path("registrations", EventResgistrationView.as_view(), name="event-registration"),
	path("registrations/<uuid:id>/", GetInvitationDetailsView.as_view(), name="event-check"),
]
