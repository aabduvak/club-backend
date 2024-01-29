from django.urls import path, include
from api.views import AuthorListView, BlogListView, BrandListView, FactListView, CategoryListView, HomeSliderListView, HomePageView

urlpatterns = [
	path("brands", BrandListView.as_view()),
	path("page/home", HomePageView.as_view())
]
