from rest_framework.serializers import ModelSerializer

from anfitriao.models import Anfitriao


class AnfitriaoSerializer(ModelSerializer):
    class Meta:
        model = Anfitriao
        fields = '__all__'
        