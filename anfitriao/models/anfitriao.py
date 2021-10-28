import uuid

from django.db import models


class Anfitriao(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
