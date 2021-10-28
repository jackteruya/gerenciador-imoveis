import datetime
import uuid

from django.db import models
from django.utils import timezone

from anfitriao.models.anfitriao import Anfitriao
from anfitriao.models.imovel import Imovel
from anfitriao.models.reserva import Reserva


class ToDo(models.Model):
    class Tarefa(models.TextChoices):
        CHECK_IN = 'check_in', 'Check In'
        CHECK_OUT = 'check_out', 'Check Out'
        LIMPEZA = 'limpeza', 'Limpeza'
        MANUTENCAO = 'manutecao', 'Manutenção'

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    data = models.DateTimeField()
    status = models.BooleanField()
    anfitriao = models.ForeignKey(Anfitriao, on_delete=models.DO_NOTHING, related_name='todos')
    tarefa = models.CharField(max_length=9, choices=Tarefa.choices, blank=False, null=False, default='')
    reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING, null=True, blank=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.DO_NOTHING, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.tarefa in (self.Tarefa.CHECK_IN, self.Tarefa.CHECK_OUT):
            self.data = self.verifica_data_reserva()

        if self._state.adding:
            self.data = self.verifica_disponibilidade()

        return super().save(*args, **kwargs)

    def verifica_data_reserva(self):
        if self.data < timezone.now():
            return ValueError("Não é possível criar data passada")
        if self.tarefa == self.Tarefa.CHECK_IN:
            data = self.reserva.data_check_in
            return data
        if self.tarefa == self.Tarefa.CHECK_OUT:
            data = self.reserva.data_check_out
            return data

    def verifica_disponibilidade(self):
        data = datetime.datetime(year=self.data.year, month=self.data.month,
                                 day=self.data.day, hour=self.data.hour, tzinfo=self.data.tzinfo)
        if ToDo.objects.filter(data=data, anfitriao=self.anfitriao).exists():
            raise ValueError("Data já preenchida")
        return self.data

