from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {
        'posts': posts
    })

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {
        'post': post
    })

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.by = request.user  # <-- automatically assign logged-in user
            post.save()
            return redirect('posts:list')

    else:
        form = PostForm()

    return render(request, 'posts/post_new.html', {
        'form': form
    })
