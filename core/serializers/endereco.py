from rest_framework.serializers import ModelSerializer

from core.models.endereco import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"