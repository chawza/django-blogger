# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('editor/<int:pk>/', views.PostEditorView.as_view(), name='post_editor'),
    path('api/preview/', views.markdown_preview, name='markdown_preview'),
]