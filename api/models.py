from django.db import models


class Invoice(models.Model):
    Customer_name = models.CharField(max_length=30)
    Invoice_id = models.CharField(max_length=100, null=True) 
    date = models.DateTimeField(auto_now_add=True)



class Invoice_details(models.Model):
    invoice = models.ForeignKey( Invoice , on_delete=models.CASCADE , null = True)
    descricption = models.TextField(blank = True , null = True)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.IntegerField()