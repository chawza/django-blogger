from django.contrib import admin
from django.urls import path
from django.conf import settings

from . import views

app_name = 'django_blogger'

urlpatterns = [
    path('editor/<int:pk>/', views.PostEditorView.as_view(), name='post_editor'),
    # path('api/preview/', views.markdown_preview, name='markdown_preview'),
]

if settings.DJANGO_BLOGGER_DEV:
    urlpatterns += [
         path('admin/', admin.site.urls)
    ]