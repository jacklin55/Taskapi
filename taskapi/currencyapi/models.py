from django.db import models

# Create your models here.
from django.db import models
from django.db import models

# Create your models here.
from django.db import models


class CurrencyModel(models.Model):
    tocurrency = models.CharField(max_length=100,null=True)
    fromcurrency = models.CharField(max_length=100,null=True)
    amount = models.CharField(max_length=100,null=True)
    rate = models.CharField(max_length=100,null=True)
    Data_currency = models.CharField(max_length=100,null=True)


