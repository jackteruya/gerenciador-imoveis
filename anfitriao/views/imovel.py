from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from anfitriao.serializers import ImovelSerializer
from anfitriao.models import Imovel


class ListarCrearImovelAPIView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer


class VerAtualizarDeletarImovelAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
