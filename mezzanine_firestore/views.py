from typing import Any

from django import http
from django.contrib.auth.decorators import login_required
from django.db.models.lookups import EndsWith
from django.http.response import HttpResponseBase, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View

from mezzanine_firestore.Forms import Patient_Form
from mezzanine_firestore.models import Paciente


class Paciente_View(View):
    initial = {'key' : 'value'}
    form_class = Patient_Form
    template_name = "mezzanine_firestore/patient.html"

    def get(self, request, *args, **kwargs):
        patient_code = self.kwargs['patient_code']
        try: 
            patient = Paciente.objects.get(id = patient_code)
            form = self.form_class(instance = patient)
        except Paciente.DoesNotExist:
            form =  self.form_class(initial = self.initial)
            patient_code = 0
        
        return render(request, self.template_name, {'form': form, 'patient_code': patient_code})

    def post(self, request, *args, **kwargs):
        patient_code = self.kwargs['patient_code']
        if 'save_page_button' in request.POST:
            try:
                instance = Paciente.objects.get(id=patient_code)
                form = self.form_class(request.POST or None, instance=instance)
            except Paciente.DoesNotExist:
                form = self.form_class(request.POST)
            if form.is_valid():
                patient = form.save()

                return render(request, 'mezzanine_firestore/paciente-guardado.html', {'patient' : patient})
            else:
                return render(request, '')

        return HttpResponseRedirect('/')

    @method_decorator(login_required)
    def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        return super(Paciente_View, self).dispatch(request, *args, **kwargs)

