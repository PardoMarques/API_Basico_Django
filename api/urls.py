from django.urls import path
from .views import (
    CarListAPIView,
    CarRetrieveAPIView,
    CarCreateAPIView,
    CarUpdateAPIView,
    CarDestroyAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Rotas de Carros
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarRetrieveAPIView.as_view(), name='car-detail'),
    path('cars/create/', CarCreateAPIView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateAPIView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDestroyAPIView.as_view(), name='car-delete'),

    # Rotas de Usuários
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),

    # Rotas de Autenticação JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]