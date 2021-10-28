from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from anfitriao.serializers import ReservaSerializer
from anfitriao.models import Reserva


class ListarCrearReservaAPIView(ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class VerAtualizarDeletarReservaAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
