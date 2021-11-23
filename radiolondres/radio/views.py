from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader
from .models import StudioRadio, PosteRadio, Message, Resistant
from .forms import diffuser_message
from django.utils.timezone import datetime



def index(request):
	template = loader.get_template('radio/index.html')
	value = "Master1 ISC TR - ETRS701_TRI Conception et programmation orientée objet - Christophe Courtin"
	context = {'message': value}
	return HttpResponse(template.render(context, request))

	#return HttpResponse("Master1 ISC TR - ETRS701_TRI Conception et programmation orientée objet - Christophe Courtin")
	


# vue studio de radio
def studioRadio(request):
	template = loader.get_template('radio/studioRadio.html')
	resistant = Resistant.objects.all()
	context = {'resistant': resistant}
	return HttpResponse(template.render(context, request))


# vue poste de radio
def posteRadio(request, pseudo):
	template = loader.get_template('radio/posteRadio.html')
	messages = Message.objects.all()
	context = {'pseudo':pseudo, 'messages':messages}
	return HttpResponse(template.render(context, request))


def displayposteRadio(request):
	template = loader.get_template('radio/posteRadio.html')
	messages = Message.objects.all()
	context = {'messages':messages, }
	return HttpResponse(template.render(context, request))

#def Resistant_has_message(request, pseudo):
def Resistant_has_message(request):
    #template = loader.get_template('radio/Resistant_has_message.html')
    #context = {'pseudo':pseudo}
    #return HttpResponse(template.render(context, request))
	return HttpResponse("resistant has message")


def diffuse_message(request):
	# s'il s'agit d'une requête POST, il faut traiter les données du formulaire
	
	if request.method == "POST":
		# créer instance de formulaire et la peupler des données de la requête
		form = diffuser_message(request.POST)
		# vérifier si elle est valide
		if form.is_valid():
			template = loader.get_template('radio/template.html')
			context = {'date_courante':datetime.now, 'form':form}
			#return HttpResponse(template.render(context, request))
			return HttpResponse("message diffuser, click <a href='/radio-londres'>ICI </a> pour diffuser un autre message")
		else:
			return HttpResponse("Le formulaire n'est pas valide. \
			cliquer <a href='/radio-londres'>ICI </a> pour remplir le formulaire.")

