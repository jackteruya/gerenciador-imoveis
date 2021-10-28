import uuid

from django.db import models

import shortuuid

from anfitriao.models import Imovel, Hospede


class Reserva(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    codigo = models.CharField(max_length=10, editable=False, unique=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.DO_NOTHING)
    hospede = models.ForeignKey(Hospede, on_delete=models.DO_NOTHING)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_check_in = models.DateTimeField()
    data_check_out = models.DateTimeField()

    def __str__(self):
        return self.codigo

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.codigo = shortuuid.random(length=10)
        return super().save(*args, **kwargs)
