from django.shortcuts import render
from django.views.generic import ListView
from .models import Clienti
from django.db.models import Count

def index(request):
    return render(request,'index.html')

class clienti(ListView):
    model = Clienti
    template_name = 'clienti_agente.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Clienti.objects.filter(agente__contains = query)
        return object_list

class sommaClienti(ListView):
    model = Clienti
    template_name = 'count.html'

    def get_queryset(request):
        object_list = Clienti.objects.all().values('agente').annotate(totale=Count('nome')).order_by()
        return object_list

