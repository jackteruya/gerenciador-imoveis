from rest_framework.serializers import ModelSerializer

from anfitriao.models import Imovel


class ImovelSerializer(ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'
