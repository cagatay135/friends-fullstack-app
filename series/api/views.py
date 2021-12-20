from rest_framework import serializers, status
from rest_framework.response import Response # redirect,render
from rest_framework.decorators import api_view
from rest_framework import viewsets


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser, AllowAny
from series.models import Character, Quote
from .serializers import CharacterSerializer, QuoteSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CharacterViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['POST','PUT','DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]

class QuoteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method in ['POST','PUT','DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]