import django_filters
from django_filters import DateFilter
from .models import *

class UserFarmersFilter(django_filters.FilterSet):
    class Meta:
        model = UserFarmers
        fields = ['farmer_number', 'member_name']
