from django.shortcuts import render, redirect
from posts.models import Post
from .forms import PostForm
# from posts.forms import PostForm
# from posts.models import Category


# def create_page(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     form = PostForm
#     return render(request, 'posts/index.html',
#                   context={
#                       'posts': form
#                   })


def main(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            category = cd.get('category')
            post = cd.get('post')
            seen = cd.get('seen')

            # Post.object.create(
            #     category=category,
            #     post=post
            # )

            category_post = Post(
                category=category,
                post=post,
                seen=seen
            )
            category_post.save()

    form = PostForm()
    return render(request, 'posts/index.html',
                  context={'form': form})
