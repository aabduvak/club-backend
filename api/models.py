from django.db import models
import uuid


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ("id",)

class Slider(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slider")

    def __str__(self) -> str:
        return self.title


class Brand(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="brand")
    url = models.URLField()
    priority = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.url


class Fact(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Team(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="team")
    designation = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Event(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to="event")
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    place = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Newsletter(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.email

class Message(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    name = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.email
