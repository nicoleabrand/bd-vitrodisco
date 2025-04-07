from rest_framework.serializers import ModelSerializer

from core.models import Gravadora

class GravadoraSerializer(ModelSerializer):
    class Meta:
        model = Gravadora
        fields = "__all__"