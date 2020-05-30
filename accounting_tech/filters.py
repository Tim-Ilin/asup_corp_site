import django_filters

from accounting_tech.models import Equipment, ReportRequestToRepair, Employees, Room


class EquipmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    date_bought = django_filters.NumberFilter(field_name='date_bought', lookup_expr='year__gt')

    class Meta:
        model = Equipment
        fields = ['name']


class ReportRequestToRepairFilter(django_filters.FilterSet):
    fio_executor = django_filters.CharFilter(field_name='fio_executor', lookup_expr='icontains')

    class Meta:
        model = ReportRequestToRepair
        fields = ['fio_executor']


class EmployeesFilter(django_filters.FilterSet):
    fio = django_filters.CharFilter(lookup_expr='icontains')
    room = django_filters.ModelChoiceFilter(queryset=Room.objects.all())

    class Meta:
        model = Employees
        fields = ['fio', 'room']
