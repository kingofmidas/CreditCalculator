from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from .serializers import CredictProductSerializer
from .models import CreditProduct


class CreditProductsView(viewsets.ModelViewSet):
    
    serializer_class = CredictProductSerializer
    queryset = CreditProduct.objects.all()
    permission_classes = (IsAdminUser,)


class CreditProductView(viewsets.ReadOnlyModelViewSet):
    
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        queryset = CreditProduct.objects.all()
        credit_product = get_object_or_404(queryset, pk=pk)
        serializer = CredictProductSerializer(credit_product)
        return Response(serializer.data)


class FilterProductView(viewsets.ReadOnlyModelViewSet):

    serializer_class = CredictProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        credit_sum = self.request.query_params.get('credit_sum')
        credit_time = self.request.query_params.get('credit_time')
        early_repayment = self.request.query_params.get('early_repayment')
     
        products = CreditProduct.objects.filter(min_credit_sum__lte=credit_sum, 
                                                max_credit_sum__gte=credit_sum,
                                                min_credit_time__lte=credit_time, 
                                                max_credit_time__gte=credit_time,
                                                early_repayment=early_repayment,
                                                )
        return products
