# Generated by Django 4.2.9 on 2024-01-31 05:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.ImageField(upload_to="brand")),
                ("url", models.URLField()),
                ("priority", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("id",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("photo", models.ImageField(upload_to="event")),
                ("date", models.DateField(blank=True, null=True)),
                ("time", models.TimeField(blank=True, null=True)),
                ("url", models.URLField(blank=True, null=True)),
                ("place", models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                "ordering": ("id",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Fact",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("number", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("id",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Slider",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="slider")),
            ],
            options={
                "ordering": ("id",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("photo", models.ImageField(upload_to="team")),
                ("designation", models.CharField(max_length=200)),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("id",),
                "abstract": False,
            },
        ),
    ]
