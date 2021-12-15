from django.urls import path
from . import views 

urlpatterns = [
    path('', views.CharacterListCreateAPIView.as_view()),
    path('<int:pk>/', views.ChracterDetailAPIView.as_view(), name='character-detail'),
    path('<int:pk>/quotes', views.QuoteListAPIView.as_view(), name='quotes'),


    # path('makaleler', views.makale_list_create_api_view),
    # path('makaleler/<int:id>', views.makale_detail_api_view),
]
