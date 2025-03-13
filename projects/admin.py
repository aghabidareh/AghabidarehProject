from django.contrib import admin
from projects.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('is_published',)
    list_display_links = ('title',)
    list_per_page = 10
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    actions = ('publish', 'private')
    exclude = ('slug',)

    def publish(self, request, queryset):
        """
        Mark selected news items as published.
        """
        queryset.update(is_published=True)

    def private(self, request, queryset):
        """
        Mark selected news items as unpublished.
        """
        queryset.update(is_published=False)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('projects.change_news'):
            actions = {key: value for key, value, in actions.items() if key in ['view_news']}
        return actions
