from django.contrib import admin

from .models import TreeModel
# Register your models here.

class TreeModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(TreeModel, TreeModelAdmin)
