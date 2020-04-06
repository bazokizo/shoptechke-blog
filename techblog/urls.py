from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
path('search/', views.SearchResultsView.as_view(), name='search_results'),

]