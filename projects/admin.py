import codecs

from django.contrib import admin
from projects.models import News

import csv
from django.http import HttpResponse


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_per_page = 10
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    readonly_fields = ('slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    actions = ('publish', 'unpublish', 'export_to_csv')

    @admin.action(description='Publish selected news items')
    def publish(self, request, queryset):
        """
        Mark selected news items as published.
        """
        queryset.update(is_published=True)

    @admin.action(description='Unpublish selected news items')
    def private(self, request, queryset):
        """
        Mark selected news items as unpublished.
        """
        queryset.update(is_published=False)

    @admin.action(description='Export selected news items to CSV')
    def export_to_csv(self, request, queryset):
        """
        Export selected news items to a CSV file.
        """
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="news_export.csv"'
        response.write(codecs.BOM_UTF8)
        writer = csv.writer(response)
        writer.writerow(['Title', 'Description', 'Is Published', 'Slug', 'Created At', 'Updated At'])
        for news in queryset:
            writer.writerow([
                news.title,
                news.description,
                news.is_published,
                news.slug,
                news.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                news.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            ])
        return response

    def get_actions(self, request):
        """
        Restrict actions based on user permissions.
        """
        actions = super().get_actions(request)
        if not request.user.has_perm('projects.change_news'):
            del actions['publish']
            del actions['unpublish']
        return actions
