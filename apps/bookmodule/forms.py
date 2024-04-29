from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title', 'author', 'price', 'edition']
        
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the title here',
                'class':'mycssclass',
                'id':'myid',
            }
        )
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        label='Author Full Name'
    )
    
    price = forms.DecimalField(
        required=True,
        min_value= 1,
        max_value = 1000,
        label='Current Price'
    )
    
    edition = forms.IntegerField(
        required=True,
        label="Edition"
    )
        
    