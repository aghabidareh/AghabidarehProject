from django.db import models

class News(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} : {self.description[:10]}"