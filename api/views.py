from rest_framework.generics import ListAPIView, RetrieveAPIView
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


class HomeSliderRetrieveView(RetrieveAPIView):
    queryset = HomeSlider.objects.all()
    serializer_class = HomeSliderSerializer

class BrandListView(ListAPIView):
    queryset = Brand.objects.order_by('created_at')
    serializer_class = BrandSerializer


class FactListView(ListAPIView):
    queryset = Fact.objects.order_by('created_at')[:4]
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
