from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from core import views as core_views

urlpatterns = [
    url(r'^index/$', core_views.index, name="index"),

    #__________________________________________GENERAL__________________________________________#
    url(r'^contactarCorreo/$', core_views.contactarCorreo, name="contactarCorreo"),
    url(r'^redactarCorreo/$', core_views.redactarCorreo, name="redactarCorreo"),
    url(r'^visualizarMensaje/$', core_views.visualizarMensaje, name="visualizarMensaje"),
    url(r'^contactarTelefono/$', core_views.contactarTelefono, name="contactarTelefono"),
    url(r'^redactarLlamada/$', core_views.redactarLlamada, name="redactarLlamada"),
    url(r'^redactarLlamada2/$', core_views.redactarLlamada2, name="redactarLlamada2"),
    url(r'^visualizarLlamada/$', core_views.visualizarLlamada, name="visualizarLlamada"),
    url(r'^visualizarContactos/$', core_views.visualizarContactos, name="visualizarContactos"),
    url(r'^registrarContacto/$', core_views.registrarContacto, name="registrarContacto"),
    url(r'^editarContacto1/$', core_views.editarContacto1, name="editarContacto1"),
    url(r'^editarContacto2/$', core_views.editarContacto2, name="editarContacto2"),
    url(r'^anularContactos/$', core_views.anularContactos, name="anularContactos"),

    #_________________________________________DIRECTOR_________________________________________#
    url(r'^directorInicio/$', core_views.directorInicio, name="directorInicio"),
    url(r'^reportesContactabilidad/$', core_views.reportesContactabilidad, name="reportesContactabilidad"),

    #________________________________________SECRETARIA________________________________________#
    url(r'^secretariaInicio/$', core_views.secretariaInicio, name="secretariaInicio"),
    url(r'^secretariaInicio2/$', core_views.secretariaInicio2, name="secretariaInicio2"),

    #________________________________________SECRETARIO________________________________________#
]
