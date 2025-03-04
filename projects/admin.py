from django.contrib import admin

from projects.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass