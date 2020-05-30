from urllib.parse import urlparse
from re import match
from django_filters.views import FilterView
from .filters import EquipmentFilter, ReportRequestToRepairFilter, EmployeesFilter
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.views.generic.base import View
from django.core import serializers

from accounting_tech.forms import RoomForm, DepartamentForm, PositionForm, RequestForm
from .models import Equipment, Employees, RequestToRepair, \
    Acquisition, ReportRequestToRepair
from .render_to_pdf import render_to_pdf


@method_decorator(login_required, name='dispatch')
class ListOfEquipment(FilterView):
    """
    This class working with list of Equipment.
    For filtering it using 3rd-party django_filters
    """
    model = Equipment
    template_name = 'accounting_tech/home.html'
    paginate_by = 10
    filterset_class = EquipmentFilter


@method_decorator(login_required, name='dispatch')
class EquipmentCreateView(CreateView):
    """In this class we're creating new kind od Equipment."""
    model = Equipment
    template_name = 'accounting_tech/create_equipment.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class EmployeesList(FilterView):
    """
    This class working with list of Employees.
    For filtering it using 3rd-party django_filters
    """
    model = Employees
    template_name = 'accounting_tech/employees_list.html'
    filterset_class = EmployeesFilter


@method_decorator(login_required, name='dispatch')
class EmployeeCreateView(CreateView):
    """In this class we're creating new kind od Equipment."""
    model = Employees
    template_name = 'accounting_tech/create_employee.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('employees_list')


class EmployeeRegisterView(CreateView):  # register new Employee same as EmployeeCreateView
    model = Employees
    template_name = 'accounting_tech/register.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('employees_list')


def list_equipment_employee(request, pk):
    """

    :param request: Come from javascript
    :param pk: Employee id
    :return: All equipment that employee have
    """
    equipment_list_of_worker_query_obj = list(Equipment.objects.filter(worker=pk))
    pin_code_of_worker_query_obj = list(Employees.objects.filter(id=pk))
    equipment_list_of_worker = serializers.serialize(
        'json', pin_code_of_worker_query_obj + equipment_list_of_worker_query_obj)
    return HttpResponse(equipment_list_of_worker)


@method_decorator(login_required, name='dispatch')
class EmployeeUpdateView(UpdateView):
    """In this class we're updating employees."""
    model = Employees
    template_name = 'accounting_tech/edit_employee.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('employees_list')


@method_decorator(login_required, name='dispatch')
class EquipmentUpdateView(UpdateView):
    """In this class we're updating equipment."""
    model = Equipment
    template_name = 'accounting_tech/edit_equipment.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('home')


class RequestToRepairCreateView(CreateView):
    """In this class we're creating new request to repair."""
    model = RequestToRepair
    template_name = 'accounting_tech/create_request_to_repair.html'
    fields = ['complainant', 'inventory_number',
              'phone', 'location', 'description_failure']

    def form_valid(self, form):
        """

        :param form: Form data
        :return: If form data valid then redirect to success_url else redirect to home
        """
        if match(r'^[0-9]-[0-9]{5}$', form.data['inventory_number']):
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return redirect('home')

    def get_success_url(self):
        """
        It send notification if data is valid
        :return: redirect to home
        """
        from notifications.signals import notify
        from django.contrib.auth.models import User, Group
        notify.send(User.objects.get(username='Admin'), recipient=Group.objects.get(name='notify'), verb='New request')
        return reverse_lazy('home')


class ReportRequestToRepairCreateView(CreateView):
    """In this class we're creating new report."""
    model = ReportRequestToRepair
    template_name = 'accounting_tech/create_report_request_to_repair.html'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        request_to_repair = RequestToRepair.objects.get(id=int(form.data['request_to_repair']))
        request_to_repair.is_repaired = True
        request_to_repair.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('list_request_to_repair')


@method_decorator(login_required, name='dispatch')
class RequestToRepairList(ListView):
    """:returns list requests to repair"""
    model = RequestToRepair

    def get_queryset(self):
        return self.model.objects.filter(is_repaired=False)

    template_name = 'accounting_tech/list_request_to_repair.html'


@method_decorator(login_required, name='dispatch')
class RequestToRepairDetail(DetailView):
    """:returns detail info about request to repair"""
    model = RequestToRepair
    template_name = 'accounting_tech/detail_request_to_repair.html'


class PrintRequestRepairToPdf(View):
    """
    This class using for print detail request to repair
    """

    def get(self, request, *args, **kwargs):
        requests = RequestToRepair.objects.filter(id=kwargs['pk'])
        from django.conf import settings
        data = {
            'root': settings.PDF_FONT_PATH,
            'requests': requests,
        }
        pdf = render_to_pdf('accounting_tech/print_request_to_repair.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class AcquisitionCreateView(CreateView):
    """This create new one of request acquisition"""
    model = Acquisition
    template_name = 'accounting_tech/create_acquisition.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class AcquisitionList(ListView):
    """List all acquisitions"""
    model = Acquisition
    template_name = 'accounting_tech/list_acquisition.html'


class FormReturnRelativePath:
    """Because i repeated that code from time to time .
    I create this class.
    It return path  relative of function, and save form.
    """

    def __init__(self, request, model_form, template):
        self.request = request
        self.model_form = model_form
        self.template = template

    def return_relative(self):
        if self.request.method == 'POST':
            form = self.model_form(self.request.POST)
            url = urlparse(self.request.POST['referrer'])
            if form.is_valid():
                form.save()
                if url:
                    if reverse('create_employee') == url.path:
                        return HttpResponseRedirect(reverse('create_employee'))
                    elif reverse('register_employee') == url.path:
                        return HttpResponseRedirect(reverse('register_employee'))
                    else:
                        return HttpResponseRedirect(url.path)

        else:
            form = self.model_form()
        return render(self.request, self.template, {'form': form})


def room_form(request):
    template = 'accounting_tech/create_room.html'
    fck = FormReturnRelativePath(request, RoomForm, template)
    return fck.return_relative()


def departament_form(request):
    template = 'accounting_tech/create_departament.html'
    fck = FormReturnRelativePath(request, DepartamentForm, template)
    return fck.return_relative()


def position_form(request):
    template = 'accounting_tech/create_position.html'
    fck = FormReturnRelativePath(request, PositionForm, template)
    return fck.return_relative()


class ReportRequestToRepairListView(FilterView):
    """List all requests to repair"""
    model = ReportRequestToRepair
    template_name = 'accounting_tech/report_request_to_repair_list.html'
    paginate_by = 10
    ordering = ['-time_field']
    filterset_class = ReportRequestToRepairFilter
