from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Post, Group, Label

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'group', 'is_published', 'created_at', 'edit_button')
    list_filter = ('content_type', 'is_published', 'group', 'labels')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('labels', 'authors')
    date_hierarchy = 'created_at'
    
    def edit_button(self, obj):
        if obj.pk:
            url = reverse('post_editor', kwargs={'pk': obj.pk})
            return format_html(
                '<a class="button" href="{}">Edit in Editor</a>',
                url
            )
        return ""
    edit_button.short_description = 'Editor'