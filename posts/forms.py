from django import forms
from posts.models.posts import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'image', 'description'}
        labels = {
            'image': 'Картинка',
            'description': 'Описание',
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')
