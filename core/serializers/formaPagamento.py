from rest_framework.serializers import ModelSerializer

from core.models import FormaPagamento

class FormaPagamentoSerializer(ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = "__all__"