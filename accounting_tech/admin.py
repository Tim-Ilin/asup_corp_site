from django.contrib import admin
from .models import Employees, Equipment, RequestToRepair, Acquisition, ReportRequestToRepair, Position, Departament, Room

admin.site.register(Employees)
admin.site.register(Equipment)
admin.site.register(RequestToRepair)
admin.site.register(Acquisition)
admin.site.register(ReportRequestToRepair)
admin.site.register(Departament)
admin.site.register(Position)
admin.site.register(Room)