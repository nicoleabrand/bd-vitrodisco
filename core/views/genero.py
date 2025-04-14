from core.models.genero import Genero
from rest_framework.viewsets import ModelViewSet
from core.serializers import GeneroSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer