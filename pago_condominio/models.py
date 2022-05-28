import datetime
from pickle import FALSE, NONE, TRUE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

# class UsuarioManager(BaseUserManager):
#     def create_user(self, email, username, nombre, apellido, password = None):
#         if not email:
#             raise ValueError("El Usuario debe tener una dirección de  Correo")
            
#         user = self.models(
#                 username = username,
#                 email = email,
#                 nombre = nombre, 
#                 apellido = apellido
#             )   
            
#         user.set_password(password)
#         user.save()
            
#         return user
        
#     def create_superuser(self, email, username, nombre, apellido, password):
#         user = self.create_user(
#             email, 
#             username = username, 
#             nombre = nombre, 
#             apellido = apellido,
#             password = password
#         )
        
#         user.usuario_administrador = True
#         user.save()
#         return user
    

class User(AbstractUser):
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=120,)
    apellido = models.CharField(max_length=120)
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=150, unique=True)
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    #objects = UsuarioManager()
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email', 'nombre', 'apellido']
    
    
    # def __str__(self):
    #     return f'{self.nombre}  {self.apellido}'
        
        
    # def has_perm(self, perm, obj = None)  :
    #     return True
        
    # def has_module_perms(self, app_label):
    #     return True
        
    # @property
    # def is_staff(self):
    #     return self.usuario_administrador
    

class Propietario(models.Model):
    cedula = models.IntegerField(default=0, unique=True)
    nombre = models.CharField(max_length=150)
    apartamento = models.IntegerField(default=0)
    piso = models.IntegerField(default=0)
    monto = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    cancelar = models.BooleanField( default=False)
    alicuota = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    
    
    def __str__(self):
        return str(self.cedula)
    
    
    # def calcular(self):
    #     return (self.monto - self.propietario.monto1)
        
    # def verifica(self):
    #     return self.cancelar == True
    
    # def save(self, *args, **kwargs):
    #     self.monto = self.calcular
    #     super(Propietario, self).save()
    
    # def save(self, *args, **kwargs):
    #     self.cancelar = self.verifica
    #     super(Propietario, self).save()
        
        
    
class Pago(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    banco = models.CharField(max_length= 25)
    num_operacion = models.IntegerField(default=0)
    fecha = models.DateField(("fecha de pago"), blank=True, null=True, default=datetime.date.today)
    monto1 = models.DecimalField(default = 0, max_digits=6, decimal_places=2)
    
    def __str__(self):
        return str(self.propietario)
