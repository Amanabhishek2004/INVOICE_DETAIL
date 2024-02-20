from rest_framework import generics
from .serializers import Invoice_serializer, Invoice_get_serializer
from .models import Invoice_details , Invoice

class InvoiceViewApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice_details.objects.all()
    serializer_class = Invoice_get_serializer
    def get_serializer(self, *args, **kwargs):
        if self.request.method == "GET":
                return Invoice_get_serializer(*args, **kwargs)
        return Invoice_serializer(*args, **kwargs)
    
class InvoiceCreateViewApi(generics.ListCreateAPIView):
    queryset = Invoice_details.objects.all()
    serializer_class = Invoice_get_serializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "POST":
           return Invoice_serializer(*args, **kwargs)
        return Invoice_get_serializer(*args, **kwargs)
    


