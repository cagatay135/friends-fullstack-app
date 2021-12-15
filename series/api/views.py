from rest_framework import serializers, status
from rest_framework.response import Response # redirect,render
from rest_framework.decorators import api_view

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from series.models import Character, Quote
from .serializers import CharacterSerializer, QuoteSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CharacterListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated|ReadOnly]


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ChracterDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

class QuoteListAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(character=self.kwargs['pk'])


"""
class CharacterListCreateAPIView(GenericAPIView):
    def get(self, request, pk=None, format=None):
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True,  context={'request': request})
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
"""

"""
class ChracterDetailAPIView(APIView):
    def get(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def put(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        serializer = CharacterSerializer(instance=character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
"""
class MakaleDetailAPIView(APIView):
    def get_object(self, id):
        makale = get_object_or_404(Makale, id=id)
        return makale

    def get(self, request, id):
        makale = self.get_object(id=id)
        serializer = MakaleSerializer(makale)
        return Response(serializer.data)
    
    def put(self, request, id):
        makale = self.get_object(id=id)
        serializer = MakaleSerializer(makale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        makale = self.get_object(id=id)
        makale.delete()
        return Response(
                status = status.HTTP_204_NO_CONTENT
            )

"""
"""
@api_view(['GET', 'POST']) # Json renderer ile uğraşmaya gerek kalmaz
def makale_list_create_api_view(request):
    if request.method == 'GET':
        makaleler = Makale.objects.filter(aktif=True)
        serializer = MakaleSerializer(makaleler, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE']) # Json renderer ile uğraşmaya gerek kalmaz
def makale_detail_api_view(request , id):
        try:
            makale = Makale.objects.get(id=id)
        except Makale.DoesNotExist:
            return Response(
                {
                    'error': {
                        'code': 404,
                        'message': f'{id} ilgili makale bulunamadı'
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )
        if request.method == 'GET':
            serializer = MakaleSerializer(makale)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = MakaleSerializer(makale, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            makale.delete()
            return Response(
                status = status.HTTP_204_NO_CONTENT
            )
""" 