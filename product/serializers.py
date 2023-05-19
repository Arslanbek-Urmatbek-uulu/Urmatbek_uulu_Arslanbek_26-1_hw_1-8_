from rest_framework import serializers
from product.models import Product, Category, Review
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()




class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = 'id title description price category'.split()



class ProductReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Review
        fields = 'product text stars'.split()




class CategoriesValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product_id stars'.split()



class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False, max_length=300)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField(min_value=1)

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist!')
        return category_id




class ReviewsValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    product_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=False)

    def validate_product_id(self, products_id):
        try:
            Product.objects.get(id=products_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist!')
        return products_id

class ReviewsCreateSerializers(serializers.Serializer):
    text = serializers.CharField()
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField()