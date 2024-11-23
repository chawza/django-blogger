from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'group', 'public', 'created')
    autocomplete_fields = ('group', 'labels')
    search_fields = ('title',)

    @admin.display(boolean=True, description='public')
    def public(self, obj):
        return not obj.private
    

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(models.Label)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ('name',)