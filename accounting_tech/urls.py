from django.conf.urls import url

from .views import *
from django.urls import path, include
from .views import ListOfEquipment, EquipmentUpdateView, list_equipment_employee, \
    RequestToRepairList, room_form, departament_form, position_form

urlpatterns = [
    path('', ListOfEquipment.as_view(), name='home'),
    path('equipment/<int:pk>/edit/',
         EquipmentUpdateView.as_view(), name='edit_equipment'),
    path('employees/<int:pk>/edit/',
         EmployeeUpdateView.as_view(), name='edit_employee'),
    path('equipment/new/',
         EquipmentCreateView.as_view(), name='create_equipment'),
    path('employee/equipment/<int:pk>/',
         list_equipment_employee, name='list_equipment_employee'),
    path('employee/new/',
         EmployeeCreateView.as_view(), name='create_employee'),
    path('employees/', EmployeesList.as_view(), name='employees_list'),
    path('request-repair/new/',
         RequestToRepairCreateView.as_view(), name='create_request_to_repair'),
    path('report-request-repair/new/',
         ReportRequestToRepairCreateView.as_view(), name='create_report_request_to_repair'),
    path('request-repair', RequestToRepairList.as_view(), name='list_request_to_repair'),
    path('request-repair/<int:pk>/', RequestToRepairDetail.as_view(), name='detail_request-repair'),
    path('print-request-repair/<int:pk>/', PrintRequestRepairToPdf.as_view(), name='print_request-repair'),
    path('print-request-list', ReportRequestToRepairListView.as_view(), name='request-to-repair-list'),
    path('acquisition/new/',
         AcquisitionCreateView.as_view(), name='create_acquisition'),
    path('acquisition', AcquisitionList.as_view(), name='list_acquisition'),
    path('register', EmployeeRegisterView.as_view(), name='register_employee'),
    path('position/new/', position_form, name='create_position'),
    path('departament/new/', departament_form, name='create_departament'),
    path('room/new/', room_form, name='create_room'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
