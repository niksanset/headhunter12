from django import forms 
from headhunter_app.models import *

class PostForm(forms.ModelForm):
    # author_post = forms.CharField(label='Author post')
    # title_post = forms.CharField(label='Title post')
    # text_post = forms.CharField(label='Text post',widget=forms.Textarea)
    # likes_post = forms.IntegerField(label='Введите сколько лайков изначально будет у поста ' )
   class Meta:
      model = Post
      fields = ('__all__')