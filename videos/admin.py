from django.contrib import admin
from videos.models import Email,Video

# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                     {'fields': ['title', 'duration', 'thumbnail']}),
        ('Youtube',                {'fields': ['youtube_id', 'published']}),
    ]

admin.site.register(Video, VideoAdmin)


class EmailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message ID',        {'fields': ['message_id']}),
        ('From',              {'fields': ['from_address']}),
        ('DateTime Recieved', {'fields': ['recieved']}),
        ('Bodies',            {'fields': ['text_body', 'html_body']}),
    ]

admin.site.register(Email, EmailAdmin)
