from django.contrib import admin
from .models import Parts, PartsRequest
from .models import Image


# Register your models here.


class PartsAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'manufacturer', 'modelName']

class PartsRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'manufacturer', 'modelName']


admin.site.register(Parts, PartsAdmin)

admin.site.register(PartsRequest, PartsRequestAdmin)

admin.site.register(Image)