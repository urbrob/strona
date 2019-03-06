from django.shortcuts import render
from .models import Person
import io
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('age') and request.POST.get('bd_date'):
            person = Person()
            person.first_name = request.POST.get('first_name')
            person.last_name = request.POST.get('last_name')
            person.age = request.POST.get('age')
            person.cd_date = request.POST.get('bd_date')
            person.save()

            return render(request, 'aboutme/index.html')

    else:
        return render(request, 'aboutme/index.html')
