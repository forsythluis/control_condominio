"""condominio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('muestra/crear/', views.PropietarioCrear.as_view(template_name = "propietarios/crear_form.html"), name='crear'),
    path('actualiza/<int:pk>', views.PropietarioActualizar.as_view(template_name = "propietarios/propietario_update_form.html"), name='actualiza'),
    path('elimina/<int:pk>', views.PropietarioElimina.as_view(template_name = "propietarios/propietario_confirm_delete.html"), name='elimina'),
    path('muestra/', views.PropietarioLista, name='muestra'),
    path('detalle/<int:pk>', views.PropietarioDetalle.as_view(template_name = "propietarios/detalle.html"), name='detalle'),
    #path('muestra/', views.muestra, name='muestra'),
    path('muestra1', views.muestra1, name='muestra1'),
    path('accounts/login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('accounts/logout', views.logout_user, name='logout'),
    path('mostrar', views.Mostrar, name='mostrar'),
    path('pagomuestra', views.PagoDetalle, name='pagomuestra'),
    path('proceso', views.Proceso, name='proceso'),
    path('muestra/saldos', views.Saldos, name='saldos'),
]