from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from .models import Company, Employee, Opening
from .serializers import CompanySerializer
# Create your views here.


class CompanyListApiView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(active=True)
    filter_backends = [SearchFilter,]
    search_fields = ['employee__role', 'opening__role']
