from rest_framework.viewsets import ModelViewSet

from core.models import Artista
from core.serializers import ArtistaSerializer

class ArtistaViewSet(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer