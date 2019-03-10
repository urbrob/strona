from django.shortcuts import render
from .models import Person
import io
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from easy_pdf.views import PDFTemplateResponseMixin
from .tasks import add_person



def index(request):
    if request.method == 'POST':
        add_person.apply_async([
            request.POST.get('first_name'),
            request.POST.get('last_name'),
            request.POST.get('age'),
            request.POST.get('bd_date'),
        ])
        return render(request, 'aboutme/thanks.html')

    else:
        return render(request, 'aboutme/index.html')

def pdf_list(request):
    return render(request, 'aboutme/pdf_list.html', {'pdfs': Person.objects.all()})


class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = Person
    template_name = 'aboutme/person.html'
