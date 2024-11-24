from django.shortcuts import render
from .models import Post


def edit_post_content(request, object_id):
    post = Post.objects.get(id=object_id)


    return render(request, 'post_edit.html', context={})