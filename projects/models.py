from django.db import models
from django.db.models import Q
from slugify import slugify


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
        """Check if the news item has an image."""
        return bool(self.image)

    def get_excerpt(self, length=20):
        """Return a shortened version of the description."""
        return self.description[:length] + ('...' if len(self.description) > length else '')

    def get_excerpt_news(self):
        """Return a shortened version of the description for related news."""
        return self.description[:50] + ('...' if len(self.description) > 50 else '')

    def get_related_news(self, limit=5):
        """
        Find related news based on title and description similarity.
        """
        words = self.title.split()
        query = Q()
        for word in words:
            query |= Q(title__icontains=word)
        return News.objects.filter(query, is_published=True).exclude(id=self.id)[:limit]

    def __str__(self):
        """
        Return a string representation of the news.
        """
        return f"{self.title} : {self.description[:10]}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, separator='-', lowercase=True, )
        super(News, self).save(*args, **kwargs)

    @classmethod
    def get_news_count(cls):
        """Return the count of all published news items."""
        return cls.objects.filter(is_published=True).count()

    @classmethod
    def get_news_by_identifier(cls, identifier):
        """
        Retrieve a news item by its primary key or slug.
        :param identifier: The primary key (int) or slug (str) of the news item.
        :return: The news item if found, otherwise None.
        """
        try:
            if isinstance(identifier, int):
                return cls.objects.filter(is_published=True, pk=identifier).first()
            else:
                return cls.objects.filter(is_published=True, slug=identifier).first()
        except (ValueError, cls.DoesNotExist):
            return None

    @classmethod
    def all_news(cls):
        return cls.objects.filter(is_published=True).order_by('-created_at')

    @classmethod
    def get_news_title(cls, identifier):
        """
        Retrieve the title of a news item by its primary key or slug.
        :param identifier: The primary key (int) or slug (str) of the news item.
        :return: The title of the news item if found, otherwise None.
        """
        news_item = cls.get_news_by_identifier(identifier)
        return news_item.title if news_item else None
