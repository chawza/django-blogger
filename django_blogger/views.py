# blog/views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

@method_decorator(staff_member_required, name='dispatch')
class PostEditorView(UpdateView):
    model = Post
    template_name = 'post_editor.html'
    fields = ['title', 'content', 'content_type', 'group', 'labels', 'authors', 'is_published']
