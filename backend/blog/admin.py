from django.contrib import admin

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status']
    list_editable = ['author', 'status']
    # autocomplete_fields = [('slug', 'title')]