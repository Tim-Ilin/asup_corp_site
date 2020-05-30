from django.forms import ModelForm
from .models import Room, Departament, Position, RequestToRepair


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_name']


class DepartamentForm(ModelForm):
    class Meta:
        model = Departament
        fields = ['departament_name']


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['position_name']


class RequestForm(ModelForm):
    class Meta:
        model = RequestToRepair
        fields = ['complainant', 'is_repaired']

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['is_repaired'].queryset = RequestToRepair.objects.filter(is_repaired=False)
