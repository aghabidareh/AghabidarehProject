from django.contrib import admin

from projects.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','description' , 'is_published')
    list_filter = ('is_published',)
    list_display_links = ('title',)
    search_fields = ('title','description')
    list_per_page = 50
    actions = ('publish',)

    def publish(self, request, queryset):
        queryset.update(is_published=True)