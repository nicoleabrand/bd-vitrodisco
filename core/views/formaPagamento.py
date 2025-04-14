from core.models import FormaPagamento
from rest_framework.viewsets import ModelViewSet
from core.serializers import FormaPagamentoSerializer

class FormaPagamentoViewSet(ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer