from turtle import width
from attr import fields
from colorama import Style
from django import forms, views
from rango.models import Category, Page
from crispy_forms.helper import FormHelper


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, widget=forms.TextInput())
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    name.widget.attrs.update({'class': 'form-control', 'size':'40' , 'placeholder':'Category Name'})
    

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title of the page', 'size':'40'}))
    url = forms.URLField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title of the page', 'size':'40'}))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
 

    def clean(self):
        cleaned_data=self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('https://' or 'http://'):
            url = 'https://' + url
            cleaned_data['url'] = url
            print(cleaned_data['url'])
            return cleaned_data


    class Meta:
        model=Page
        exclude = ('category',)

    
