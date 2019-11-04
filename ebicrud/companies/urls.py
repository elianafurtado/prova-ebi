from django.urls import path
from .views import list_companies, create_company, update_company, delete_company,list_service_orders

urlpatterns = [
    path('',list_companies,name='list_companies'),
    path('new/',create_company,name='create_company'),
    path('update/<int:id>',update_company,name='update_company'),
    path('dele/<int:id>',delete_company,name='delete_company'),
    path('so/<int:id>',list_service_orders,name='list_service_orders'),
]
