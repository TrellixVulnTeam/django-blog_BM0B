from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_new.html', {'form': form})


def post_delete(request, pk):
    posts = Post.objects.all()
    post = Post.objects.get(pk=pk)
    post.delete()
    return render(request, 'blog/post_list.html', {'posts': posts})