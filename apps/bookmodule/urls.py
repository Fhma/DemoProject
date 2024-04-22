from django.urls import path, re_path
from apps.bookmodule import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('books', views.books, name = "books"),
    path('book/<int:bId>', views.book, name="book"),
    path('addBook', views.addBook, name='addBook'),
    path('updateBook/<int:bId>', views.updateBook, name="updateBook"),
    path('filterbooks', views.filterbooks, name="filterbooks")
]