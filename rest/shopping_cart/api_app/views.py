from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .models import CartItem
class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class CartItemsList(APIView):
    def get(self, request):
        cart_items = CartItem.objects.all()
        cart_items_serializer = CartItemSerializer(cart_items,many=True) 
        return Response(cart_items_serializer.data) 


# Create your views here.
