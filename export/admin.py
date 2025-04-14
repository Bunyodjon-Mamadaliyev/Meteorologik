from django.contrib import admin
from django.utils.html import format_html
from .models import Export

@admin.register(Export)
class ExportAdmin(admin.ModelAdmin):
    list_display = ('user', 'export_type', 'status', 'created_at', 'completed_at', 'file_link')
    list_filter = ('status', 'export_type', 'created_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at', 'completed_at')
    ordering = ('-created_at',)

    def file_link(self, obj):
        if obj.file:
            return format_html("<a href='{}' target='_blank'>Yuklab olish</a>", obj.file.url)
        return "-"
    file_link.short_description = "Fayl"
