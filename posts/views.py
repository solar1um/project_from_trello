from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Category


def create_page(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = PostForm
    return render(request, 'index/base.html',
                  context={
                      'posts': form
                  })
