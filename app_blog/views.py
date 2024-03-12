from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment, Category
from .forms import CommentForm


def home(request):
    posts = Post.objects.all()

    return render(request, 'app_blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'app_blog/about.html')

def detail(request, category_slug, slug ):
    post = get_object_or_404(Post, category_slug=category_slug, slug=slug)

    if request.method =='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=slug)

    else: 
        form = CommentForm()

    return render(request, 'app_blog/details.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug )
    return render(request, 'app_blog/category.html', {'category': category})