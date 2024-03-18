from django.urls import path, re_path
from apps.bookmodule import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('books', views.books, name = "books"),
    path('book/<int:bId>', views.book),
    path('filterbooks', views.filterbooks, name="filterbooks")
]