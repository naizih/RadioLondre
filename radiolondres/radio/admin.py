from django.contrib import admin

# Register your models here.



from .models import StudioRadio, Resistant, Message, PosteRadio


admin.site.register(Message)
admin.site.register(StudioRadio)
admin.site.register(Resistant)
admin.site.register(PosteRadio)