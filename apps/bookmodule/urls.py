from django.urls import path, re_path
from apps.bookmodule import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('books', views.books),
    path('book/<int:bId>', views.book)
]