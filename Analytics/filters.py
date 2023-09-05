import django_filters
from django_filters import DateTimeFilter, CharFilter
from .models import OcuppiedSpace

class OccupiedSpaceFilter(django_filters.FilterSet):
    start_date = DateTimeFilter(field_name="occupied_at", label="Fecha desde: AAAA/MM/DD ", lookup_expr='gte')
    end_date = DateTimeFilter(field_name="unoccupied_at", label="Fecha hasta: AAAA/MM/DD", lookup_expr='lte')
    class Meta:
        model = OcuppiedSpace
        fields = ['space_id']
