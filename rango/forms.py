from attr import fields
from django import forms, views
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,help_text="Please Enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


    def clean(self):
        cleaned_data=self.cleaned_data

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url']= url

            return cleaned_data

    class Meta:
        model=Page
        exclude = ('category',)

    
