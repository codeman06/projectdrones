from django.contrib import admin
from .models import Category, Photo,Upload,Report
# Register your models here.

admin.site.register(Report)
admin.site.register(Category)
admin.site.register(Photo)

class ReportInline(admin.StackedInline):
    model  = Report

class UploadAdmin(admin.ModelAdmin):
    inlines = [ReportInline,]
admin.site.register(Upload,UploadAdmin)