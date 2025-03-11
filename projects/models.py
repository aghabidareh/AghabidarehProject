from django.db import models
from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    image = models.ImageField(upload_to='news/', blank=True, null=True)

    slug = models.SlugField(unique=True, max_length=64, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'News'
        verbose_name = 'News'

    def has_image(self):
        return bool(self.image)

    def get_excerpt(self, length=50):
        return self.description[:length] + ('...' if len(self.description) > length else '')

    def __str__(self):
        return f"{self.title} : {self.description[:10]}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @classmethod
    def get_sum_of_news(cls):
        return cls.objects.filter(is_published=True).count()

    @classmethod
    def get_news_by_pk(cls, pk):
        try:
            return cls.objects.filter(is_published=True, pk=pk).first()
        except:
            return None

    @classmethod
    def get_news_by_slug(cls, slug):
        try:
            return cls.objects.filter(is_published=True, slug=slug).first()
        except:
            return None

    @classmethod
    def all_news(cls):
        return cls.objects.filter(is_published=True).order_by('-created_at')

    @classmethod
    def get_title_of_a_news(cls, pk):
        try:
            return cls.objects.filter(is_published=True, pk=pk).first().title
        except:
            return None
