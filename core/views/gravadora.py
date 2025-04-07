from rest_framework.viewsets import ModelViewSet

from core.models import Gravadora
from core.serializers import GravadoraSerializer

class GravadoraViewSet(ModelViewSet):
    queryset = Gravadora.objects.all()
    serializer_class = GravadoraSerializer