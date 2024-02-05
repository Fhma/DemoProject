from django.urls import path, re_path
from apps.bookmodule import views

urlpatterns = [    
    path('', views.index, name='index'),
]