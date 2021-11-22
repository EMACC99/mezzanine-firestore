from django.db.models import fields
from plugin_example.models import Paciente, models
class Patient_Form():
    class Meta:
        model = Paciente
        fields = ['first_name', 'last_name', 'genero_otro', 'gender', 'fecha_nacimiento', 'country', 'weight', 'heigth']