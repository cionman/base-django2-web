from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # dummy = forms.CharField(widget=NaverMapPointWidget(attrs={'width': "100%", 'height': 200}))

    class Meta:
        model = Post
        fields = '__all__'


