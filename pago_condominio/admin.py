from django.contrib import admin
from .models import Propietario, Pago, User

# Register your models here.
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apartamento', 'piso', 'monto', 'cancelar', 'alicuota')
    
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'username', 'password', 'email')
     
admin.site.register(Propietario, PropietarioAdmin)
admin.site.register(Pago)
admin.site.register(User, UserAdmin)
