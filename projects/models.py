from django.db import models


class News(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'News'
        verbose_name = 'News'

    def __str__(self):
        return f"{self.title} : {self.description[:10]}"

    @classmethod
    def get_sum_of_news(cls):
        return cls.objects.filter(is_published=True).count()

    @classmethod
    def get_news_by_pk(cls , pk):
        try:
            return cls.objects.filter(is_published=True).get(pk=pk)
        except:
            return None

    @classmethod
    def all_news(cls):
        return cls.objects.filter(is_published=True).order_by('-created_at')