from django.db import models

# Create your models here.

class Account(models.Model):
    pass

class Payment(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='payments')
    amount=models.IntegerField()
