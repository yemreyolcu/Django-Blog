from django.contrib import admin

from .models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","date"]
    list_display_links = ["title","author","date"]
    search_fields = ["title"]
    class Meta:
        model = Article
