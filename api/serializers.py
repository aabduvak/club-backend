from rest_framework import serializers
from api.models import Slider, Brand, Fact, Team, Event


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ["id", "created_at", "updated_at"]


class SliderSerializer(BaseModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class BrandSerializer(BaseModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class FactSerializer(BaseModelSerializer):
    class Meta:
        model = Fact
        fields = "__all__"


class TeamSerializer(BaseModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class EventSerializer(BaseModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"