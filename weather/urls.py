from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,  name='index'), # requests for main page, this requests will be processed by function index in views
    path('delete/', views.delete_first_city, name='delete_first_city'), # this name can be used in templates or in code for creating links
]