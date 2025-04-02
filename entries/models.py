from django.db import models
from django.utils.text import slugify

class Entry(models.Model):
    title = models.CharField(max_length = 128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    slug = models.SlugField(unique = True, blank = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete = models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.entry.title}"