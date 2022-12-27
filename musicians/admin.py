from django.contrib import admin
from .models import Artist
from .models import Album
from .models import Lyric
from .models import Song
# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Lyric)
admin.site.register(Song)