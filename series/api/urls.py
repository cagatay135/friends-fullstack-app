from django.urls import path, include
from . import views 
from rest_framework import routers, permissions


from .views import CharacterViewSet, QuoteViewSet

# We are registering our viewset(controllers) to the routers
router = routers.DefaultRouter()
router.register(r'character', CharacterViewSet)
router.register(r'quote', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
