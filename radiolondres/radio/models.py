from django.db import models
import datetime
# Create your models here.


class StudioRadio (models.Model):
    messageCourant_text = models.CharField(max_length=255, blank=True)

class Resistant (models.Model):
    pseudo = models.CharField(max_length=45, blank=True)
    studioRadio = models.ForeignKey(StudioRadio,on_delete=models.CASCADE, blank=True)



class Message(models.Model):
    message_text = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField(default=datetime.date, null=True, blank=True)



class Resistant_has_message(models.Model):
    resistant_id = models.ForeignKey(Resistant, on_delete=models.CASCADE, blank=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE, blank=True)


class Action(models.Model):
    action_text = models.CharField(max_length=45, blank=True)
    #message_id = models.ForeignKey(Message,on_delete=models.CASCADE, blank=True)
    message_id = models.OneToOneField(Message, on_delete=models.CASCADE, blank=True)



class PosteRadio (models.Model):
    messageCourant_text =  models.CharField(max_length=255, blank=True)
    StudioRadio_id = models.ForeignKey(StudioRadio,on_delete=models.CASCADE, blank=True)


class GroupeClandestin(models.Model):
    pseudo = models.CharField(max_length=45)
    messageAttendu_text = models.CharField(max_length=255, blank=True)
    #PosteRadio_id = models.ForeignKey(PosteRadio,on_delete=models.CASCADE, blank=True)
    PosteRadio_id = models.OneToOneField(PosteRadio,on_delete=models.CASCADE)



class Envahisseur(models.Model):
    pseudo = models.CharField(max_length=45, blank=True)
    #PosteRadio_id = models.ForeignKey(PosteRadio,on_delete=models.CASCADE,blank=True)
    PosteRadio_id = models.OneToOneField(PosteRadio, on_delete=models.CASCADE)