from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from anfitriao.serializers import ToDoSerializer, ToDoAnfitriaoSerializer
from anfitriao.models import ToDo, Anfitriao


class ListarCrearToDoAPIView(ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class VerAtualizarDeletarToDoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


# Lista todos os anfitriões com os a fazeres
class ListarToDoAnfitriaoAPIVew(ListAPIView):
    queryset = Anfitriao.objects.all()
    serializer_class = ToDoAnfitriaoSerializer


# Lista apenas um afitriao com os a fazeres
class VerToDoAnfitriaoAPIVew(RetrieveAPIView):
    queryset = Anfitriao.objects.all()
    serializer_class = ToDoAnfitriaoSerializer


