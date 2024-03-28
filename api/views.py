from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from api.utils import generate_qrcode

from api.models import Slider, Brand, Fact, Team, Event, Newsletter, Message, EventRegistration
from api.serializers import (
    SliderSerializer,
    BrandSerializer,
    FactSerializer,
    TeamSerializer,
    EventSerializer,
    MessageSerializer,
    NewsLetterSerializer,
    EventRegistrationSerializer
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
            Message:\n{text}
            """

            sender_email = settings.EMAIL_HOST_USER
            receiver_email = settings.EMAIL_RECEIVER

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
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            server.login(sender_email, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        serializer = MessageSerializer(message)
        return Response(serializer.data)

class CollectEmailView(APIView):
    serializer_class = NewsLetterSerializer

    def post(self, request):
        return Response(status=200)

class EventResgistrationView(ListCreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if EventRegistration.objects.exists(email=request.data['email']):
           instance = EventRegistration.objects.get(email=request.data['email'])
           serializer = self.get_serializer(data=instance)
           return Response(serializer.data, status=status.HTTP_200_OK)
         
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        instance = EventRegistration.objects.get(email=request.data['email'])
        qr_content = f"https://technovasyon.pythonanywhere.com/api/v1/registrations/{instance.id}"
        filename = f"files/uploads/invitation/{instance.id}.png"
        
        generate_qrcode(qr_content, filename)
        
        subject = "TECH24 Zirvesi Biletiniz"
        body = f"Merhabalar {instance.name}\nTECH24 Zirvesi katılım formunu doldurduğuz için teşekkür ederiz. Zirve günü aşağıdaki QR kod yardımıyla giriş yapabilirsiniz.\n\nGörüşmek üzere Teknoloji ve İnovasyon Topluluğu"

        sender_email = settings.EMAIL_HOST_USER

        # Create a MIMEText object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = instance.email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=invitation_{instance.id}.png",
            )
            msg.attach(part)

        # SMTP server settings
        smtp_server = settings.EMAIL_HOST
        smtp_port = 465  # or 465 for SSL

        # Start a secure SMTP connection
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(sender_email, instance.email, msg.as_string())
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GetInvitationDetailsView(RetrieveAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
