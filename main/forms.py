from django.forms import ModelForm
from django import forms
from .models import Book
    
class BookForm(ModelForm):
    title = forms.TextInput()
    author = forms.TextInput()
    genre = forms.TextInput()
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']