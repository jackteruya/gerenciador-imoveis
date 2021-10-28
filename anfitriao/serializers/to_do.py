from rest_framework import serializers

from anfitriao.models import ToDo, Anfitriao


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoAnfitriaoSerializer(serializers.ModelSerializer):

    todos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ver-atualizar-deletar-to-do')

    class Meta:
        model = Anfitriao
        fields = (
            'id',
            'nome',
            'todos',
        )
