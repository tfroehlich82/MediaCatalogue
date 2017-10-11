from django.contrib import admin
from watson.admin import SearchAdmin
from .models import Image, Video, Audio, Category, GenericObjectRelation, RelationType


class ImageAdmin(SearchAdmin):
    search_fields = ("full_path", )


class VideoAdmin(SearchAdmin):
    search_fields = ("full_path", )


class AudioAdmin(SearchAdmin):
    search_fields = ("full_path", )


class CategoryAdmin(admin.ModelAdmin):
    pass


class RelationAdmin(admin.ModelAdmin):
    pass


class RelationTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RelationType, RelationTypeAdmin)
admin.site.register(GenericObjectRelation, RelationAdmin)

