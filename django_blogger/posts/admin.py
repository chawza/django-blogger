from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html

# Register your models here.
from . import models
from . import views

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'group', 'public', 'created', 'edit')
    autocomplete_fields = ('group', 'labels')
    search_fields = ('title',)

    @admin.display(boolean=True, description='public')
    def public(self, obj):
        return not obj.private
    
    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path(
                "<path:object_id>/change-content/",
                views.edit_post_content,
                name="change-content",
            ),
        ]
        print(urls)
        return urls

    def edit(self, obj):
        return format_html('<a href="%s">%s</a>' % reverse('django_blogger:posts:edit-content', obj.id), 'edit')
    

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.Label)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)