from django.contrib import admin

# Register your models here.



from .models import StudioRadio, Resistant, Message, PosteRadio, Resistant_has_message, Action, GroupeClandestin, Envahisseur, FlotteAllie, SaboteurFerroviaire


admin.site.register(Message)
admin.site.register(StudioRadio)
admin.site.register(Resistant)
admin.site.register(PosteRadio)
admin.site.register(Resistant_has_message)
admin.site.register(Action)
admin.site.register(GroupeClandestin)
admin.site.register(Envahisseur)
admin.site.register(FlotteAllie)
admin.site.register(SaboteurFerroviaire)
