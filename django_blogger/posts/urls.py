from django.contrib import admin
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('edit-content', views.edit_post_content, name='edit-content')
]
