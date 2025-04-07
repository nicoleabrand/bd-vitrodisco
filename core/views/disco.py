from rest_framework.viewsets import ModelViewSet

from core.models import Disco
from core.serializers import DiscoSerializer

class DiscoViewSet(ModelViewSet):
    queryset = Disco.objects.all()
    serializer_class = DiscoSerializer