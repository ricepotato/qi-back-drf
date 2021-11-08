from rest_framework import viewsets
from .models import Market
from .serializers import MarketModelSerializer


class MarketModelViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.order_by("-pk").all()
    serializer_class = MarketModelSerializer
