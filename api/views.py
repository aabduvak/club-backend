from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
            body = f"""
            User: {name}
            Email: {email}
            Message:
            {text}
            """

            sender_email = settings.EMAIL_HOST_USER
            receiver_email = 'abdulaziz.yosk@gmail.com'

            # Create a MIMEText object
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # SMTP server settings
            smtp_server = settings.EMAIL_HOST
            smtp_port = 465  # or 465 for SSL

            # Start a secure SMTP connection
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, settings.EMAIL_HOST_PASSWORD)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                print('Email sent successfully')
        serializer = MessageSerializer(message)
        return Response(serializer.data)

class CollectEmailView(APIView):
    serializer_class = NewsLetterSerializer
    
    def post(self, request):
        return Response(status=200)
