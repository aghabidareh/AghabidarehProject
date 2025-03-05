from django.contrib import admin

from projects.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('is_published',)
    list_display_links = ('title',)
    list_per_page = 50
    list_editable = ('is_published',)
    search_fields = ('title','description')
    actions = ('publish','private')

    def publish(self, request, queryset):
        queryset.update(is_published=True)

    def private(self, request, queryset):
        queryset.update(is_published=False)