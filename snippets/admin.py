from django.contrib import admin
from .models import Snippet
# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ['highlighted']

# admin.site.register(Snippet, SnippetAdmin)
