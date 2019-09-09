#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from core.models import *
import datetime
import json
import os
import requests
import ast
from unidecode import unidecode
from django.conf import settings
from django.template.loader import get_template
#import StringIO
import os
from io import BytesIO
from django.template.loader import get_template

#__________________________INDEX__________________________#
def index(request):
    """template_name = "index.html"
    request.session['rol'] = 'DC'"""

    template_name = "autenticar/login.html"
    email = str(request.POST['email'])
    passw = str(request.POST['password'])
    if email == "hayde@unab.cl" and passw == "admin":
        template_name = "secretaria/inicio.html"
        request.session['rol'] = 'SECRETARIA'
    elif email == "eduardo@unab.cl" and passw == "admin":
        template_name = "director/inicio.html"
        request.session['rol'] = 'DIRECTOR'

    return render(request,template_name,{})

#__________________________LOGIN__________________________#
def login(request):
    template_name = "autenticar/login.html"
    return render(request, template_name,{})
def crearCuenta(request):
    template_name = "autenticar/crearCuenta.html"
    return render(request, template_name,{})
def recuperarContrasena(request):
    template_name = "autenticar/recuperarContrasena.html"
    return render(request, template_name,{})

#__________________________GENERAL__________________________#
def contactarCorreo(request):
    template_name = "general/contactarCorreo.html"
    return render(request, template_name,{})
def redactarCorreo(request):
    template_name = "general/redactarCorreo.html"
    return render(request, template_name,{})
def visualizarMensaje(request):
    template_name = "general/visualizarMensaje.html"
    return render(request, template_name,{})
def contactarTelefono(request):
    template_name = "general/contactarTelefono.html"
    return render(request, template_name,{})
def redactarLlamada(request):
    template_name = "general/redactarLlamada.html"
    return render(request, template_name,{})
def redactarLlamada2(request):
    template_name = "general/redactarLlamada2.html"
    return render(request, template_name,{})
def visualizarLlamada(request):
    template_name = "general/visualizarLlamada.html"
    return render(request, template_name,{})
def visualizarContactos(request):
    template_name = "general/visualizarContactos.html"
    return render(request, template_name,{})
def registrarContacto(request):
    template_name = "general/registrarContacto.html"
    return render(request, template_name,{})
def editarContacto1(request):
    template_name = "general/editarContacto1.html"
    return render(request, template_name,{})
def editarContacto2(request):
    template_name = "general/editarContacto2.html"
    return render(request, template_name,{})
def anularContactos(request):
    template_name = "general/anularContactos.html"
    return render(request, template_name,{})
#_________________________DIRECTOR_________________________#
def directorInicio(request):
    template_name = "director/inicio.html"
    return render(request, template_name,{})
def reportesContactabilidad(request):
    template_name = "director/reportesContactabilidad.html"
    return render(request, template_name,{})
#________________________SECRETARIA________________________#
def secretariaInicio(request):
    template_name = "secretaria/inicio.html"

    """template_name = "autenticar/login.html"
    email = str(request.POST['email'])
    passw = str(request.POST['password'])
    if email == "hayde@unab.cl" and passw == "admin":
        template_name = "secretaria/inicio.html"""

    return render(request, template_name,{})
def secretariaInicio2(request):
    template_name = "secretaria/inicio2.html"
    return render(request, template_name,{})

#________________________SECRETARIO________________________#
