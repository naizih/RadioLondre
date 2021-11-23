
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('radio-londres/', views.studioRadio, name="radio-londres"),
    path('poste-radio/<int:pseudo>/', views.posteRadio),
    path('diffuser_message', views.diffuse_message, name='diffuser_message'),
    path('Resistant_has_message', views.Resistant_has_message, name='Resistant_has_message'),
    path('poste-radio', views.displayposteRadio),
]