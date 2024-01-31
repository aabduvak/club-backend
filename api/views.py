from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Slider, Brand, Fact, Team, Event
from api.serializers import (
    SliderSerializer,
    BrandSerializer,
    FactSerializer,
    TeamSerializer,
    EventSerializer
)


class SliderListView(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer



class BrandListView(ListAPIView):
    queryset = Brand.objects.order_by("created_at")
    serializer_class = BrandSerializer


class FactListView(ListAPIView):
    queryset = Fact.objects.order_by("created_at")[:4]
    serializer_class = FactSerializer


class TeamListView(ListAPIView):
    queryset = Team.objects.order_by("order")
    serializer_class = TeamSerializer


class TeamShortListView(ListAPIView):
    queryset = Team.objects.order_by("created_at")[:3]
    serializer_class = TeamSerializer


class EventListView(ListAPIView):
    queryset = Event.objects.order_by("-created_at")
    serializer_class = EventSerializer

class MessageCreateView(APIView):
    def post(self, request):
        return Response(status=200)

class CollectEmailView(APIView):
    def post(self, request):
        return Response(status=200)
