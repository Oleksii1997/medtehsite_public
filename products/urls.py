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
from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

#app_name = 'products'

urlpatterns = [
    path('sub_category/', views.sub_category_products_page, name="sub_category"),
    path('sub_category/<int:sub_category_id>', views.category_products_page, name="category"),

    path('category/<int:category_id>', views.products_some_category, name="product_some_category"),
    path('category/<int:category_id>/page/<int:page_now_number>', views.products_some_category, name="some_category_paginator"),
   
    path('category/product_id/<int:product_id>', views.product_page, name="selected_product"),

    path('filtration_result/', views.product_filter, name="product_filter"),
    path('filtration_result/<int:page_now_number>', views.product_filter, name="filter_result_paginator"),
]
#(?P<category_id>\w)/$ <int:category_id>
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)