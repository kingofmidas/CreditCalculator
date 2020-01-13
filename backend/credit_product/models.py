from django.db import models
from django.shortcuts import reverse


class CreditProduct(models.Model):

    name = models.CharField(max_length=124)
    credit_rate = models.IntegerField()
    min_credit_time = models.IntegerField()
    max_credit_time = models.IntegerField()
    min_credit_sum = models.DecimalField(max_digits=8, decimal_places=2)
    max_credit_sum = models.DecimalField(max_digits=8, decimal_places=2)
    early_repayment = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    
    