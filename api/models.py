from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de Usuário padrão do Django

class Car(models.Model):
    make = models.CharField("Marca", max_length=50)
    model = models.CharField("Modelo", max_length=50)
    year = models.PositiveIntegerField("Ano")
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    description = models.TextField("Descrição", blank=True)
    owner = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de Atualização", auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
