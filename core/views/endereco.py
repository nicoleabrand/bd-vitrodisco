from core.models.endereco import Endereco
from rest_framework.viewsets import ModelViewSet
from core.serializers.endereco import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer