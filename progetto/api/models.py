from django.db import models
from tastypie.resources import ModelResource
from app.models import Clienti
# Create your models here.

class Resource(ModelResource):
    class Meta:
        queryset = Clienti.objects.all()
        resource_name = 'risorsa'