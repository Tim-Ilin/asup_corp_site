from django.db import models, migrations
from django.urls import reverse


class Position(models.Model):
    position_name = models.CharField(max_length=50, blank=False, verbose_name='Должность')

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = "Должности"


class Departament(models.Model):
    departament_name = models.CharField(max_length=50, blank=False, verbose_name='Отдел')

    def __str__(self):
        return self.departament_name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = "Отделы"


class Room(models.Model):
    room_name = models.CharField(max_length=50, blank=False, verbose_name='Кабинет')

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = "Кабинеты"


class Employees(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=False, verbose_name='Фамилия')
    surname = models.CharField(max_length=50, blank=False, verbose_name='Отчество')
    fio = models.CharField(max_length=150, blank=False, verbose_name='Ф.И.О.(Полностью)')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    pin_code = models.IntegerField(blank=False, verbose_name='Пинкод')
    post = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, verbose_name="Должность")
    dept = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True, verbose_name="Отдел")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, verbose_name="Кабинет")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = "Работники"


class Equipment(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Наименование')
    description = models.CharField(max_length=100, blank=True, verbose_name='Описание')
    inventory_number = models.CharField(max_length=100, blank=True, verbose_name='ИНВ №')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name='IP адрес')
    date_bought = models.DateField(blank=False, verbose_name='Дата постановки')
    worker = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = "Техника"

    def get_absolute_url(self):
        return reverse('detail_equipment', kwargs={'pk': self.pk})


class RequestToRepair(models.Model):
    complainant = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, verbose_name='Заявитель')
    inventory_number = models.CharField(max_length=50, blank=False, verbose_name='ИНВ №')
    phone = models.CharField(max_length=20, blank=False, verbose_name='Телефон')
    location = models.CharField(max_length=100, blank=False, verbose_name='Местонахождение')
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Время создания заявки')
    description_failure = models.TextField(max_length=200, blank=True, verbose_name='Краткое описание неисправности')
    is_repaired = models.BooleanField(default=False, verbose_name='выполнено')

    def __str__(self):
        return self.complainant.fio

    class Meta:
        verbose_name = 'Заявку на ремонт'
        verbose_name_plural = "Заявки на ремонт"


class ReportRequestToRepair(models.Model):
    request_to_repair = models.ForeignKey(RequestToRepair, on_delete=models.CASCADE, null=True, verbose_name='Заявитель', limit_choices_to={'is_repaired': False})
    fio_executor = models.CharField(max_length=150, blank=False, verbose_name='ФИО исполнителя')
    post = models.CharField(max_length=100, blank=False, verbose_name='Должность исполнителя')
    time_field = models.DateTimeField(auto_now=True, verbose_name='Дата и время')
    report = models.TextField(max_length=600, blank=False, verbose_name='Отчет')

    def __str__(self):
        return self.request_to_repair.complainant.fio

    class Meta:
        verbose_name = 'Отчет по заявке на ремонт'
        verbose_name_plural = 'Отчеты по заявкам на ремонт'


class Acquisition(models.Model):
    complainant = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, verbose_name='Заявитель')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    description_acquisition = models.TextField(max_length=100, blank=True, verbose_name='Краткое описание заявки')
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Время создания заявки')

    def __str__(self):
        return self.complainant.fio

    class Meta:
        verbose_name = 'Заявку на приобретение'
        verbose_name_plural = 'Заявки на приобретение'
