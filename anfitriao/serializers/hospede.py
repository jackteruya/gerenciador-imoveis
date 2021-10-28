from rest_framework.serializers import ModelSerializer

from anfitriao.models import Hospede


class HospedeSerializer(ModelSerializer):
    class Meta:
        model = Hospede
        fields = '__all__'
