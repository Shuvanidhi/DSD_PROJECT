from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .bigquery_client import run_query
from .models import Customer, Product, Transaction
from .serializers import CustomerSerializer, ProductSerializer, TransactionSerializer

class CustomerListView(APIView):
    def get(self, request):
        # BigQuery SQL Query
        query = "SELECT * FROM `savvy-cinema-444321-g4.dsd_project_data.customer` LIMIT 10"
        data = run_query(query)
        if data:
            return Response(data)
        else:
            return Response({"error": "Failed to fetch customer data"}, status=500)

class ProductListView(APIView):
    def get(self, request):
        query = "SELECT * FROM `savvy-cinema-444321-g4.dsd_project_data.product` LIMIT 10"
        data = run_query(query)
        return Response(data)

class TransactionListView(APIView):
    def get(self, request):
        query = "SELECT * FROM `savvy-cinema-444321-g4.dsd_project_data.transactions` LIMIT 10"
        data = run_query(query)
        return Response(data)


