from django.contrib import admin
from watson.admin import SearchAdmin
from .models import Image, Video, Audio, Category


class ImageAdmin(SearchAdmin):
    search_fields = ("full_path", )


class VideoAdmin(SearchAdmin):
    search_fields = ("full_path", )


class AudioAdmin(SearchAdmin):
    search_fields = ("full_path", )


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Category, CategoryAdmin)

