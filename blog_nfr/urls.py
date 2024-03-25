from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from blog_nfr.sitemaps import CategorySitemap, PostSitemap 


from django.contrib import admin
from django.urls import path, include
from app_blog import urls

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

    path('admin/', admin.site.urls),
    path('', include('app_blog.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
