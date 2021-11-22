from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import StudioRadio, PosteRadio
from .forms import contact_us_Form
from django.utils.timezone import datetime



def index(request):
	return HttpResponse("Master1 ISC TR - ETRS701_TRI Conception et programmation orientée objet - Christophe Courtin")



# vue studio de radio
def studioRadio(request):
    template = loader.get_template('radio/studioRadio.html')
    context = {}
    return HttpResponse(template.render(context, request))


# vue poste de radio
def posteRadio(request, pseudo):
    template = loader.get_template('radio/posteRadio.html')
    context = {'pseudo':pseudo}
    return HttpResponse(template.render(context, request))


def contact_us(request):
	# s'il s'agit d'une requête POST, il faut traiter les données du formulaire
	if request.method == "POST":
		# créer instance de formulaire et la peupler des données de la requête
		form = contact_us_Form(request.POST)
		# vérifier si elle est valide
		if form.is_valid():
			template = loader.get_template('radio/template.html')
			context = {'date_courante':datetime.now, 'form':form}
			return HttpResponse(template.render(context, request))
		else:
			return HttpResponse("Le formulaire n'est pas valide.")
