from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from django.db.models import Q 

from .models import Post, Comment, Category
from .forms import CommentForm


def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    paginate_by = 1 

    return render(request, 'app_blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'app_blog/about.html')

def detail(request, category_slug, slug ):
    post = get_object_or_404(Post, slug=slug, status = Post.ACTIVE)

    if request.method =='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", category_slug=category_slug, slug=slug)

    else: 
        form = CommentForm()

    return render(request, 'app_blog/details.html', {'post': post, 'form': form})


def category(request, slug):
    categories = Category.objects.filter(slug=slug)
    
    if categories.exists():
        category = categories.first()
        active_posts = category.category_posts.filter(status=Post.ACTIVE)
        context = {
            'category': category,
            'posts': active_posts
        }
    else:
        context = {
            'category': None,
            'posts': [],
            'error_message': 'Cette catégorie n\'est pas enregistrée dans la base de données.'
        }
    
    return render(request, 'app_blog/category.html', context)

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'app_blog/search.html', {'posts': posts, 'query': query})


def robots_txt(request):
    text= [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type='text/plain')