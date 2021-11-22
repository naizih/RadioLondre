
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('radio-londres/', views.studioRadio),
    path('poste-radio/<int:pseudo>/', views.posteRadio),
    path('contact', views.contact_us, name='contact'),
]