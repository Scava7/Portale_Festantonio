from django.http import HttpResponse
from django.template import loader
from .models import Iscrizione

def view_iscrizioni(request):
    iscrizioni_tornei = Iscrizione.objects.all()
    template = loader.get_template('iscrizioni.html')
    context = {
        'iscrizioni_tornei': iscrizioni_tornei,
    }
    return HttpResponse(template.render(context, request))

def view_details(request, id):
  iscritto = Iscrizione.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'iscritto': iscritto,
  }
  return HttpResponse(template.render(context, request))


def view_main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())



def view_testpage(request):
    iscrizioni_tornei = Iscrizione.objects.filter(first_name='Andrea').values()|Iscrizione.objects.filter(first_name='Giovanni').values()
    template = loader.get_template('test_page.html')
    context = {
        'iscrizioni_tornei': iscrizioni_tornei,
    }
    return HttpResponse(template.render(context, request))