from rest_framework import serializers
from .models import CreditProduct


class CredictProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditProduct
        fields = '__all__'