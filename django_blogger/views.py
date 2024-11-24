# blog/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import markdown
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

@method_decorator(staff_member_required, name='dispatch')
class PostEditorView(UpdateView):
    model = Post
    template_name = 'blog/post_editor.html'
    fields = ['title', 'content', 'content_type', 'group', 'labels', 'authors', 'is_published']
