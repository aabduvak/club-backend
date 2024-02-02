from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

from api.models import Slider, Brand, Fact, Team, Event, Newsletter, Message
from api.serializers import (
    SliderSerializer,
    BrandSerializer,
    FactSerializer,
    TeamSerializer,
    EventSerializer,
    MessageSerializer,
    NewsLetterSerializer
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
    serializer_class = MessageSerializer
    def post(self, request):
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        text = request.data.get('message', '')
        
        if not name or not email or not text:
            return Response({"status":"error", "message": "invalid input"}, status=400)

        message, created = Message.objects.get_or_create(name=name, email=email, content=text)
        if created:
            subject = "New message from technovasyon.com"
            content = f"""
            User: {name}
            Email: {email}
            Message:
            {text}
            """
            send_mail(subject, content, "technovasyon.com", ["abdulaziz.abduvakhobov@technovasyon.com"])
        serializer = MessageSerializer(message)
        return Response(serializer.data)

class CollectEmailView(APIView):
    serializer_class = NewsLetterSerializer
    
    def post(self, request):
        return Response(status=200)
