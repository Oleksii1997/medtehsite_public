"""medtehsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView


urlpatterns = [
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('device/', include('device_info.urls')),
    path('office/', include('user_office.urls')),
    path('products_repair/', include('products_repair.urls')),
    path('about_us/', views.about_us, name="about_us"),
    path('how_work/', views.how_we_work, name="how_we_work"),
    path('summernote/', include('django_summernote.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)