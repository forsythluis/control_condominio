from decimal import Decimal
import time
from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Propietario,  Pago
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth import login as login_process, logout, authenticate
from .form import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            messages.success(request, 'Usuario Creado Correctamente') 
            return redirect('home')
        else:
            messages.success(request, 'Error, Verifica tus datos. ')
            return redirect('register')
    else:
        form = SignupForm()
    return render(request, 'registration/registro.html', {'form': form})
     
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Gracias, Usted ha salido del sistema ')
    return redirect('home') 
    
    
def login(request):
        form = LoginForm(request.POST or None)
        msg = None
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username, password = password)
                print(user)
                if user is not None and user.is_staff:
                    login_process(request, user)
                    return redirect('muestra')
                elif user is not None:
                    login_process(request, user)
                    return redirect('muestra1')
                else:
                    messages.success(request, 'Credenciales Inválidas')
                    return redirect('login')
            else:
                messages.success(request, 'Error Validando el Formulario')
        return render(request, 'propietarios/muestra.html', {'form' : form, 'msg': msg})
        
        
@login_required
def muestra(request):
    return render(request, 'propietarios/muestra.html')
    
    
def home(request):
    return render(request, 'propietarios/index.html')
    
    
@login_required
def muestra1(request):
    return render(request, 'propietarios/muestra1.html')
    
            
@login_required
def  PropietarioLista(request):
    model = Propietario
    propietarios =  Propietario.objects.order_by('cedula')
    cantidad =Propietario.objects.count()
    print(cantidad)
    page_number = request.GET.get('page')
    paginator = Paginator(propietarios, 5)  
    print(page_number)
    try:
       page_obj = paginator.page(page_number)
       
    except PageNotAnInteger:
    
        page_obj = paginator.page(1)
        
    except EmptyPage:
    
        page_obj = paginator.page(paginator.num_pages)
    contexto = {
          
          'propietarios' : propietarios,
          'page_obj': page_obj,
          'cantidad': cantidad,
    }
    
    return render(request, 'propietarios/muestra.html', contexto)
    
    
    
class PropietarioDetalle(DetailView):
    model = Propietario
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)  
        return  context
       
     
     
     
class PropietarioCrear(SuccessMessageMixin, CreateView):
    model = Propietario
    form = Propietario
    fields = "__all__"
    success_message ="Propietario creado Correctamente"
    
    
    def get_success_url(self):
        return reverse("muestra")
        
        
        
        
class PropietarioActualizar(SuccessMessageMixin,UpdateView):
    model = Propietario
    form = Propietario
    fields= "__all__"
    template_name_suffix = 'update_form'
    success_message = "Propietario Actualizado Correctamente"
    
    def get_success_url(self):
        return reverse("muestra")
             
             
             
             
class PropietarioElimina(SuccessMessageMixin, DeleteView):
    model = Propietario
    template_name = 'propietario_confirm_delete.html'
    success_url=reverse_lazy("muestra")
    
    

    
    
        
    
 
 
def  Mostrar(request):
    if  request.POST.get('cedula'):
         ced = int(request.POST.get('cedula'))
         propi = Propietario.objects.all()
         propi = propi.filter(cedula = ced)
    
    return render(request, 'propietarios/muestra1.html', {'Propietario': propi, 'cedula': ced})

   
def PagoDetalle(request):
    model = Propietario
    propi = Propietario.objects.all()
    if  request.method == 'POST':
         ced = int(request.POST['cedula'])
         mont = request.POST['monto']
         propi = propi.filter(cedula=ced)         
    return render(request, 'propietarios/detalle_pago.html', {'Propietario': propi, 'cedula': ced, 'monto': mont})


def Proceso(request):
    if request.method == 'POST':
        # ced = int(request.POST['cedula'])
        # banco = request.POST['banco']
        # operacion = request.POST['operacion']
        # fecha = request.POST['fecha']
        # monto = request.POST['monto']
        # propie = Propietario.objects.all()
        # pro = propie.filter(cedula = ced)
        # print(pro)
        # print(ced)
        # print(operacion)
        # print(fecha)
        # print(monto)
        # print(banco)
        tipo = Propietario.objects.get(cedula = request.POST['cedula'])
        pago = Pago()
        pago.propietario = tipo
        pago.banco = request.POST['banco']
        pago.num_operacion = request.POST['operacion']
        pago.fecha = request.POST['fecha']
        pago.monto1 = request.POST['monto']
        actualiza = Propietario()
        inicio = actualiza.monto
        tipo.monto = float(tipo.monto) - float(request.POST['monto'])
        tipo.cancelar = True
        pago.save()
        tipo.save()
        return redirect(muestra1)
        
        

def Saldos(request):
    if request.method == 'POST':
        saldo = float(request.POST['saldos'])
        a = float(2.40)
        b = float(4.0)
        c = float(5.80)
        d = float(7.80)
        tot = Propietario.objects.all()
        actua = Propietario()
        #print(tot)
        for total in tot:
            s=0
            e=0
            e=float(total.alicuota)
            s=total.monto
            if e == a:
                s = float(s) + (saldo * a)/100
                total.monto = s
                total.save()
            else :
              if e == b:    
                 s = float(s) + (saldo * b)/100
                 total.monto = s
                 total.save()
              else:
                if e == c:
                   s = float(s) + (saldo * c)/100
                   total.monto = s
                   total.save()
                else:
                  if e == d:
                     s = float(s) + (saldo * d)/100
                     total.monto = s
                     total.save()
    return  redirect("muestra")  
