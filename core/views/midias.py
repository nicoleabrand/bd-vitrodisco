from rest_framework.viewsets import ModelViewSet

from core.models import Midias
from core.serializers import MidiasSerializer

class MidiasViewSet(ModelViewSet):
    queryset = Midias.objects.all()
    serializer_class = MidiasSerializer