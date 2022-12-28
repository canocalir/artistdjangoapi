from django.urls import path
from .views import (
    musicians, 
    artist_list, 
    artist_create, 
    artist_update, 
    artist_delete, 
    album_list,
    album_create,
    album_delete,
    album_update,
    song_list,
    song_create,
    song_update,
    song_delete,
    lyric_list,
    lyric_create,
    lyric_update,
    lyric_delete
    )

urlpatterns = [
    path("", musicians),
    path("artists-list", artist_list, name="list"),
    path("artist-create", artist_create, name="create"),
    path("artist-update/<int:pk>", artist_update, name="update"),
    path("artist-delete/<int:pk>", artist_delete, name="delete"),
    path("albums-list", album_list, name="list"),
    path("album-create", album_create, name="create"),
    path("album-update/<int:pk>", album_update, name="update"),
    path("album-delete/<int:pk>", album_delete, name="delete"),
    path("songs-list", song_list, name="list"),
    path("song-create", song_create, name="create"),
    path("song-update/<int:pk>", song_update, name="update"),
    path("song-delete/<int:pk>", song_delete, name="delete"),
    path("lyrics-list", lyric_list, name="list"),
    path("lyric-create", lyric_create, name="create"),
    path("lyric-update/<int:pk>", lyric_update, name="update"),
    path("lyric-delete/<int:pk>", lyric_delete, name="delete")

]
