
from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('category_repair/', views.category_repair_page, name="category_repair"),
    path('category_repair/<int:category_repair_id>', views.repair_some_category, name="repair_some_category"),
    path('consultation_repair', views.need_consultation, name="need_consultation"),

]
#(?P<category_id>\w)/$ <int:category_id>
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)