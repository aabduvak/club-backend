from django.urls import path
from api.views import (HomeSliderListView, BrandListView, FactListView, TeamListView,
                    MediaListView, AuthorListView, CategoryListView, TagListView, BlogListView)

urlpatterns = [
    path('sliders/', HomeSliderListView.as_view(), name='home-sliders-list'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('facts/', FactListView.as_view(), name='fact-list'),
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('media/', MediaListView.as_view(), name='media-list'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
]
	