from django.db import models
from mptt.models import  MPTTModel

# Create your models here.


class TreeModel(MPTTModel):


    parent = models.ForeignKey('self', on_delete=models.PROTECT ,  null=True, blank=True, related_name='children')
    code = models.CharField( max_length=20,null=True, blank=True)
    remarks = models.TextField(verbose_name='opmerkingen', blank=True, null=True)