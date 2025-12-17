from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug', 'banner']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Post title'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 6,
                'placeholder': 'Write post content...'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'post-slug'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your comment...',
                'class': 'comment-textarea'
            })
        }
