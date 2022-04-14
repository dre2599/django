from csv import list_dialects
from django.contrib import admin
from .models import Clienti

# Register your models here.

class AdminClienti(admin.ModelAdmin):
    list_display = ('id','nome','indirizzo','telefono','agente')

admin.site.register(Clienti,AdminClienti)