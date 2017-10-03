from django.contrib import admin
from watson.admin import SearchAdmin
from .models import Image


class ImageAdmin(SearchAdmin):
    search_fields = ("full_path", )


admin.site.register(Image, ImageAdmin)
