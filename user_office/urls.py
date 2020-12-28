from django.urls import path
from.import views

urlpatterns = [
	path('user_orsers/', views.view_orders, name="office_view_orders"),
	path('my_repairs/', views.view_repair, name="office_view_repair"),
	path('my_repairs/<int:repair_id>', views.user_device_repair_info, name="user_device_repair_info"),
	path('my_repairs/PDF/<int:repair_id>',views.datatable_Repair_PDF, name="datatable_Repair_PDF"),
]
