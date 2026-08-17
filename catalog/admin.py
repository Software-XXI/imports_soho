from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ("name", "section", "price", "image", "active")
    list_display = ("name", "section", "price", "created_at", "active", "image_preview")
    list_filter = ("section", "active")
    search_fields = ("name",)
    list_editable = ("price", "active")
    list_per_page = 20

    @admin.display(description="Imagen")
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="60" height="60" style="object-fit:cover;border-radius:6px;" />'
        return "—"

    image_preview.allow_tags = True