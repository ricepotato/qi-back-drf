from rest_framework import viewsets
from .models import Company
from .serializers import CompanyModelSerializer


class CompanyModelViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.order_by("-pk").all()
    serializer_class = CompanyModelSerializer
