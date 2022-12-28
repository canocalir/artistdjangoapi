from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, LyricSerializer

from .models import Artist, Album, Song, Lyric


@api_view()
def musicians(request):
    return Response('home: This is the musicians page...')

# Artist Views


@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def artist_create(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Artist created succesfully'
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def artist_update(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f"Artist is updated successfully"
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def artist_delete(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    artist.delete()
    message = {
        "message": f"Artist deleted succesfully"
    }
    return Response(message)

# Album Views


@api_view(['GET'])
def album_list(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def album_create(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Album created succesfully'
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def album_update(request, pk):
    album = get_object_or_404(Album, id=pk)
    serializer = ArtistSerializer(instance=album, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f"Artist is updated successfully"
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def album_delete(request, pk):
    album = get_object_or_404(Album, id=pk)
    album.delete()
    message = {
        "message": f"Artist deleted succesfully"
    }
    return Response(message)


# Song Views

@api_view(['GET'])
def song_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def song_create(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Song created succesfully'
        }
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def song_update(request, pk):
    song = get_object_or_404(Song, id=pk)
    serializer = SongSerializer(instance=song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f"Song is updated successfully"
        }
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def song_delete(request, pk):
    song = get_object_or_404(Song, id=pk)
    song.delete()
    message = {
        "message": f"Song deleted succesfully"
    }
    return Response(message)

# Lyric Views


@api_view(['GET'])
def lyric_list(request):
    lyrics = Lyric.objects.all()
    serializer = LyricSerializer(lyrics, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def lyric_create(request):
    serializer = LyricSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Lyric created succesfully'
        }
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def lyric_update(request, pk):
    lyric = get_object_or_404(Lyric, id=pk)
    serializer = LyricSerializer(instance=lyric, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Lyric is updated successfully'
        }
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def lyric_delete(request):
    song = get_object_or_404(Lyric, id=pk)
    song.delete()
    message = {
        "message": f'Lyric deleted successfully'
    }
    return Response(message)
