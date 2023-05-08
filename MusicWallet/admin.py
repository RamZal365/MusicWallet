from django.contrib import admin

# Register your models here.
from .models import Song, Note, Bar

admin.site.register(Song)
admin.site.register(Note)
admin.site.register(Bar)
