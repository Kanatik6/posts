from django_filters import rest_framework as django_filters

from apps.posts import models


class DateLikeFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(
        field_name='time__date', lookup_expr='gte')
    date_to = django_filters.DateFilter(
        field_name='time__date', lookup_expr='lte')

    class Meta:
        model = models.Like
        fields = ['date_from', 'date_to']


class DateDisLikeFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(
        field_name='time__date', lookup_expr='gte')
    date_to = django_filters.DateFilter(
        field_name='time__date', lookup_expr='lte')

    class Meta:
        model = models.DisLike
        fields = ['date_from', 'date_to']
