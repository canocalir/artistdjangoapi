from rest_framework import serializers
from .models import Artist, Album, Lyric, Song

# Artist Serializer


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "first_name", "last_name", "artist_pic", "num_stars"]

# Album Serializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)

    class Meta:
        model = Album
        fields = ["artist", "name", "cover", "released"]

# Lyric Serializer


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ["title", "content"]

# Song Serializer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["album", "artist", "name", "released", "lyric"]
