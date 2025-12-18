from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.db.models import Count,Q
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def posts_list(request):
    posts = (
        Post.objects
        .filter(is_published=True)
        .select_related("author")
        .annotate(
            total_comments=Count(
                'comments',
                filter=Q(comments__is_active=True)
            )
        )
        .order_by('-created_at')
    )

    return render(request, 'posts/posts_list.html', {
        'posts': posts
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)

    comments = Comment.objects.filter(
        post=post,
        parent__isnull=True,
        is_active=True
    ).order_by("-created_at")

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)

        if form.is_valid():
            parent = None
            parent_id = request.POST.get("parent_id")

            if parent_id:
                parent = Comment.objects.filter(id=parent_id).first()

            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.parent = parent
            comment.save()

            return redirect("posts:page", slug=slug)

    else:
        form = CommentForm()

    return render(request, "posts/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
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
