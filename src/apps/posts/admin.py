from django.contrib import admin
from .models import Subject, Topic


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "title", "created_at", "updated_at")
    list_display_links = list_display
    list_filter = ("subject",)
    search_fields = ("title", "body")
