from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from anfitriao.serializers import AnfitriaoSerializer
from anfitriao.models import Anfitriao


class ListarCriarAnfitriaoAPIView(ListCreateAPIView):
    queryset = Anfitriao.objects.all()
    serializer_class = AnfitriaoSerializer


class VerAtualizarDeletarAnfitriaoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Anfitriao.objects.all()
    serializer_class = AnfitriaoSerializer
