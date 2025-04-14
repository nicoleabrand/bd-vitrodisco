from rest_framework.serializers import ModelSerializer

from core.models import Midias

class MidiasSerializer(ModelSerializer):
    class Meta:
        model = Midias
        fields = "__all__"