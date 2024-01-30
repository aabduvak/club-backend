from rest_framework import serializers
from api.models import HomeSlider, Brand, Fact, Team, Media, Author, Category, Tag, Blog


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ["id", "created_at", "updated_at"]


class HomeSliderSerializer(BaseModelSerializer):
    class Meta:
        model = HomeSlider
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


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            "id",
            "created_at",
            "updated_at",
            "rcImage",
            "gridImage",
            "largeImage",
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        base_url = request.build_absolute_uri('/')[:-1] if request else ''
        representation = super().to_representation(instance)

        # Update the image fields to include full URLs
        for field in ['rcImage', 'gridImage', 'largeImage']:
            if representation.get(field):
                representation[field] = f"{representation[field]}"

        return representation


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(BaseModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class BlogSerializer(BaseModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Blog
        exclude = ('body',)
