from rest_framework.serializers import ModelSerializer

from core.models import Disco

class DiscoSerializer(ModelSerializer):
    class Meta:
        model = Disco
        fields = "__all__"