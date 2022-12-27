from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializer

from .models import Artist


@api_view()
def musicians(request):
    return Response('home: This is the musicians page...')


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
