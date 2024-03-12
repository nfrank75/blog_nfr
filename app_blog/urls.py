from django.urls import path
from .views import home, about, detail, category

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='post_detail'),
    path('<slug:slug>/', category, name='post_detail'),
]