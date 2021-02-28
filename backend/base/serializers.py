from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken

from base.models import Product, Review, Order, OrderItem, ShippingAddress


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "_id", "username", "email", "name", "isAdmin"]

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "_id", "username", "email", "name", "isAdmin", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)

        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product objects."""

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("_id",)


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for review objects. """

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ("_id",)


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for order objects."""

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("_id",)


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for order item objects."""

    class Meta:
        model = OrderItem
        fields = "__all__"
        read_only_fields = ("_id",)


class ShippingAddressSerializer(serializers.ModelSerializer):
    """Serializer for shipping address objects."""

    class Meta:
        model = ShippingAddress
        fields = "__all__"
        read_only_fields = ("_id",)
