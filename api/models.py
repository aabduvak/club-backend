from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HomeSlider(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slider")

    def __str__(self) -> str:
        return self.title


class Brand(BaseModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="brand")
    url = models.URLField()
    priority = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.url


class Fact(BaseModel):
    title = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Team(BaseModel):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="team")
    designation = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    rcImage = models.ImageField(upload_to="blogs", null=True, blank=True)
    gridImage = models.ImageField(upload_to="blogs", null=True, blank=True)
    largeImage = models.ImageField(upload_to="blogs", null=True, blank=True)


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Blog(BaseModel):
    media = models.ForeignKey(
        Media, related_name="blog", null=True, blank=True, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, related_name="blog", null=True, blank=True, on_delete=models.SET_NULL
    )
    published_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="blogs")
    body = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.author.get_full_name()}"
