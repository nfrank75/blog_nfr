from django.urls import path
from .views import home, about, detail, category, search, robots_txt


urlpatterns = [
    path('robots_txt', robots_txt, name='robots_txt'),
    path('', home, name='home'),
    path('about', about, name='about'),
    
    path('search/', search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='post_detail'),
    path('<slug:slug>/', category, name='category_detail'),
] 