from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import HomeSlider, Brand, Fact, Team, Media, Author, Category, Tag, Blog
from api.serializers import (
    HomeSliderSerializer,
    BrandSerializer,
    FactSerializer,
    TeamSerializer,
    MediaSerializer,
    AuthorSerializer,
    CategorySerializer,
    TagSerializer,
    BlogSerializer,
)

class HomeSliderListView(ListAPIView):
    queryset = HomeSlider.objects.all()
    serializer_class = HomeSliderSerializer


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FactListView(ListAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MediaListView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class HomePageView(APIView):
    def get(self, request):
        slider = HomeSlider.objects.last()
        brands = Brand.objects.order_by('-created_at')[:4]
        facts = Fact.objects.order_by('-created_at')[:4]
        team = Team.objects.order_by('order')[:3]
        
        data = {
            "slider": HomeSliderSerializer(slider).data,
            "brands": BrandSerializer(brands, many=True).data,
            "facts": FactSerializer(facts, many=True).data,
            "team": TeamSerializer(team, many=True).data
        }
        return Response(data)