from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('add_device/', views.new_device, name="new_device_form"),
	path('add_device_user_maked/', views.maked_device_user, name="maked_new_device_user"),
	path('add_device_maked/', views.maked_device, name="maked_new_device"),
	path('all_devices/', views.all_device_database, name="all_device_database"),
	path('inform_repair/', views.inform_repair, name="inform_repair"),
	path('advertising_mail/', views.advertising_mail, name="advertising_mail"),
	path('user_devices/', views.view_user_devices, name="view_user_devices"),
	path('all_active_devices/', views.all_device_database_active, name="all_device_database_active"),
	path('add_device/unpaid_repair_device', views.unpaid_repair_device, name="unpaid_repair_device"),
	path('all_client/', views.all_client, name="all_client_database"),
	path('update_device/<int:device_id>', views.updated_device_info, name="updated_device_info"),
	path('add_device/search_user', views.search_user, name="search_user"),
	path('add_device/search_type_device', views.search_type_device, name="search_type_device"),
	path('add_device/search_model_device', views.search_model_device, name="search_model_device"),
	path('add_device/add_type_model', views.add_type_model, name="add_type_model"),
]
#(?P<category_id>\w)/$ <int:category_id>
