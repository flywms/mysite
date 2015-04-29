from django.contrib import admin
from daodejing.models import *


class DaodejAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Daodej,DaodejAdmin)

# Register your models here.
