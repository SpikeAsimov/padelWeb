from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import Turno

def turnos(request):
    misturnos = Turno.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'misturnos': misturnos,
    }
    return HttpResponse(template.render(context, request))

