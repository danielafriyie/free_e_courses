from django.contrib import admin
from .models import ECourses, Contact, TopAd, BottomAd


@admin.register(ECourses)
class ECoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date')
    list_display_links = ('id', 'title')
    list_filter = ('date', 'category')
    search_fields = ('id', 'title', 'date')
    list_per_page = 25


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'date')
    list_display_links = ('id', 'name')
    list_filter = ('date',)
    search_fields = ('id', 'name', 'email', 'date')
    list_per_page = 25


@admin.register(TopAd)
class TopAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name')
    list_filter = ('date',)
    search_fields = ('id', 'name', 'date')
    list_per_page = 25


@admin.register(BottomAd)
class BottomAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name')
    list_filter = ('date',)
    search_fields = ('id', 'name', 'date')
    list_per_page = 25
