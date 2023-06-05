from shopping.models import Product, Review
# from rest_framework.response import Response
# from rest_framework import status\
from rest_framework import viewsets
# from rest_framework.views import APIView
from .serializers import ProductSerializer, ReviewSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, mixins
class ReviewAV(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
class ProductVS(viewsets.ModelViewSet):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # def get(self, request):
    #     movies = Product.objects.all()
    #     serializer = ProductSerializer(movies, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
        
    #     serializer = ProductSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
