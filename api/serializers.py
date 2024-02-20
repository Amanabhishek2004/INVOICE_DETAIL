from rest_framework import serializers
from .models import Invoice, Invoice_details
import uuid

class Invoice_serializer(serializers.Serializer):
    Customer_name = serializers.CharField()
    quantity = serializers.IntegerField()
    unit_item_price = serializers.IntegerField()
    

    def create(self, validated_data):
        customer_name = validated_data["Customer_name"]
        quantity = validated_data["quantity"]
        unit_item_price = validated_data["unit_item_price"]
        total_price = quantity * unit_item_price
      
        random_uuid = uuid.uuid4()
        hex_uuid = random_uuid.hex

        # Create an Invoice instance
        instance = Invoice.objects.create(
            Customer_name=customer_name,
            Invoice_id=str(hex_uuid)
        )
            
        data =  Invoice_details.objects.create(                          
            invoice=instance,
            quantity=quantity,
            unit_price=unit_item_price,
            total_price=total_price                                   
        )

        return data
        
    def update(self, instance, validated_data):
    # Update attributes of the Invoice_details instance
     instance.quantity = validated_data.get("quantity", instance.quantity)
     instance.unit_price = validated_data.get("unit_item_price", instance.unit_price)
     instance.total_price = instance.quantity * instance.unit_price
    
    # Update attributes of the related Invoice instance (if needed)
     if instance.invoice:
        instance.invoice.Customer_name = validated_data.get("customer_name", instance.invoice.Customer_name)
        instance.invoice.save()

     instance.save()
     return instance



class invoice_inline_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"

class Invoice_get_serializer(serializers.ModelSerializer):
    invoice = invoice_inline_Serializer()
    class Meta:
        model = Invoice_details
        fields = "__all__"


