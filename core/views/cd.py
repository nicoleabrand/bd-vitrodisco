from rest_framework.viewsets import ModelViewSet

from core.models import Cd
from core.serializers import CdSerializer

class CdViewSet(ModelViewSet):
    queryset = Cd.objects.all()
    serializer_class = CdSerializer