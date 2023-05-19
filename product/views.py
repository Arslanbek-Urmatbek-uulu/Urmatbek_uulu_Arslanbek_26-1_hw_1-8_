from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializers, \
    ProductReviewSerializer, ProductValidateSerializer, ReviewsValidateSerializer, ReviewsCreateSerializers
from product.models import Product, Category, Review
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView

class CategoriesAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'



class ReviewsAPIViews(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsValidateSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        data_dict = ReviewSerializers(reviews, many=True).data
        return Response(data=data_dict)

    def post(self, request, *args, **kwargs):
        serializers = ReviewsValidateSerializer(data=request.data)
        if not serializers.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializers.errors)
        product_id = serializers.validated_data.get('product_id')
        stars = serializers.validated_data.get('stars')
        text = serializers.validated_data.get('text')
        review = Review.objects.create(product_id=product_id, text=text, stars=stars)
        return Response(data=ReviewSerializers(review).data)



class ReviewsDetailAPIViews(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsValidateSerializer
    lookup_field = 'id'



class ProductsAPIViews(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        data_dict = ProductSerializer(products, many=True).data
        return Response(data=data_dict)

    def post(self, request, *args, **kwargs):
        serializers = ProductValidateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializers.errors)
        title = serializers.validated_data.get('title')
        description = serializers.validated_data.get('description')
        price = serializers.validated_data.get('price')
        category_id = serializers.validated_data.get('category_id')
        product = Product.objects.create(
            title=title, description=description, price=price, category_id=category_id)
        return Response(data=ProductSerializer(product).data)






class ProductsDetailAPIViews(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=id)
        data_dict = ProductSerializer(product, many=False).data
        return Response(data=data_dict)

    def put(self, request, *args, **kwargs):
        product = Product.objects.get(id=id)
        serializers = ProductValidateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializers.errors)
        product.title = serializers.validated_data.get('title')
        product.description = serializers.validated_data.get('description')
        product.price = serializers.validated_data.get('price')
        product.category_id = serializers.validated_data.get('category_id')
        product.save()
        return Response(data=ProductSerializer(product).data)



class ProductsReviewsAPIViews(ListAPIView):
    serializer_class = ReviewSerializers
    def get(self, request, *args, **kwargs):
        products_reviews = Review.objects.all()
        average_stars = Review.objects.aggregate(Avg('stars'))
        data_dict = ProductReviewSerializer(products_reviews, many=True).data
        return Response(data=[data_dict, average_stars])

