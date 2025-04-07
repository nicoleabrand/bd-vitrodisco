from rest_framework.serializers import ModelSerializer

from core.models import Cd

class CdSerializer(ModelSerializer):
    class Meta:
        model = Cd
        fields = "__all__"