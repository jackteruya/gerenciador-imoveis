from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from anfitriao.serializers import HospedeSerializer
from anfitriao.models import Hospede


class ListarCrearHospedeAPIView(ListCreateAPIView):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer


class VerAtualizarDeletarHospedeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer
