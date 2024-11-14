from rest_framework import generics, permissions
from ..models import Car
from ..serializers import CarSerializer
from ..permissions import IsOwnerOrReadOnly

# Views de Carros

# Queries (Leitura)
class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Commands (Escrita)
class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CarUpdateAPIView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.owner:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Você não tem permissão para atualizar este carro.")

class CarDestroyAPIView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_destroy(self, instance):
        if self.request.user == instance.owner:
            instance.delete()
        else:
            raise permissions.PermissionDenied("Você não tem permissão para deletar este carro.")