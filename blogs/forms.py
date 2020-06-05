from django import forms
from .models import Blog, Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())
    name = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ('content', 'name')