from django_filters import rest_framework as filters
from .models import Product, Review, Order, Collection


class ProductFilter(filters.FilterSet):
    price = filters.RangeFilter()
    desc = filters.CharFilter(
        field_name='description',
        lookup_expr='in'
    )
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='in'
    )

    class Meta:
        model = Product
        fields = ['price', 'description', 'name']


class ReviewFilter(filters.FilterSet):
    user_id = filters.ModelChoiceFilter(
        field_name='user',
        to_field_name='user',
        queryset=Review.objects.all(),
    )
    product = filters.ModelChoiceFilter(
        field_name='product',
        to_field_name='product',
        queryset=Product.objects.all(),
    )
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Review
        fields = ['user', 'created_at', 'product']


class OrderFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = ['status', 'order_value', 'created_at', 'updated_at', 'items']