from shopping.models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductSerializer


class ProductAV(APIView):

    def get(self, request):
        movies = Product.objects.all()
        serializer = ProductSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
