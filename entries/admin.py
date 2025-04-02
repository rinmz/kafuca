from django.contrib import admin
from .models import Entry, Comment

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Entry)
admin.site.register(Comment)
