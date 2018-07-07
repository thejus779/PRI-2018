from django.contrib import admin
from .models import Parts
from .models import Image


# Register your models here.


class PartsAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'manufacturer', 'modelName']


admin.site.register(Parts, PartsAdmin)

admin.site.register(Image)