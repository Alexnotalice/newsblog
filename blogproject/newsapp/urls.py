from django.urls import  path 
from . import views

urlpatterns = [
    path('',views.web_data,name='cnews'),    
]