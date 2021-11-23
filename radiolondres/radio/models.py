from django.db import models
import datetime
# Create your models here.


class StudioRadio (models.Model):
    messageCourant_text = models.CharField(max_length=255)

class Resistant (models.Model):
    pseudo = models.CharField(max_length=45, blank=True)
    studioRadio = models.ForeignKey(StudioRadio,on_delete=models.CASCADE)



class Message(models.Model):
    message_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField()



class Resistant_has_message(models.Model):
    resistant_id = models.ForeignKey(Resistant, on_delete=models.CASCADE)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)


class Action(models.Model):
    action_text = models.CharField(max_length=45, blank=True)
    #message_id = models.ForeignKey(Message,on_delete=models.CASCADE, blank=True)
    message_id = models.OneToOneField(Message, on_delete=models.CASCADE)



class PosteRadio (models.Model):
    messageCourant_text =  models.CharField(max_length=255)
    StudioRadio_id = models.ForeignKey(StudioRadio,on_delete=models.CASCADE)


class GroupeClandestin(models.Model):
    pseudo = models.CharField(max_length=45)
    messageAttendu_text = models.CharField(max_length=255, blank=True)
    #PosteRadio_id = models.ForeignKey(PosteRadio,on_delete=models.CASCADE, blank=True)
    PosteRadio_id = models.OneToOneField(PosteRadio,on_delete=models.CASCADE)



class Envahisseur(models.Model):
    pseudo = models.CharField(max_length=45, blank=True)
    #PosteRadio_id = models.ForeignKey(PosteRadio,on_delete=models.CASCADE,blank=True)
    PosteRadio_id = models.OneToOneField(PosteRadio, on_delete=models.CASCADE)


class FlotteAllie(models.Model):
	pseudo = models.CharField(max_length=25)
	resistant_id = models.ForeignKey(Resistant,on_delete=models.CASCADE)



class SaboteurFerroviaire(models.Model):
    pseudo = models.CharField(max_length=25)
    groupeClandestin_id = models.ManyToManyField(GroupeClandestin)
