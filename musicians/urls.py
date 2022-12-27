from django.urls import path
from .views import musicians, artist_list, artist_create, artist_update, artist_delete

urlpatterns = [
    path("", musicians),
    path("artists-list", artist_list, name="list"),
    path("artist-create", artist_create, name="create"),
    path("artist-update/<int:pk>", artist_update, name="update"),
    path("artist-delete/<int:pk>", artist_delete, name="delete")
]
