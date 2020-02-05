#for pdf upload download
from django import forms
from .models import Book

class OurForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'name', 'pdf')
    