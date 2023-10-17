import django_filters
from .models import OcuppiedSpace
from django import forms
from django_filters import DateFromToRangeFilter


class OccupiedSpaceFilter(django_filters.FilterSet):
    start = django_filters.DateFilter(field_name='occupied_at', lookup_expr='gte', label='Fecha inicial',widget=forms.DateInput(attrs={'type': 'date'}))
    end = django_filters.DateFilter(field_name='occupied_at', lookup_expr='lte', label='Fecha final',widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = OcuppiedSpace
        exclude = ['occupied_at', 'unoccupied_at', 'id']
