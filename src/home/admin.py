from django.contrib import admin
from .models import Parts, PartsRequest, Contact
from .models import Image


# Register your models here.


class PartsAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'manufacturer', 'modelName']

class PartsRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'manufacturer', 'modelName']

class ContactAdmin(admin.ModelAdmin):
        list_display = ['name', 'email', 'subject', 'message']


admin.site.register(Parts, PartsAdmin)

admin.site.register(PartsRequest, PartsRequestAdmin)

admin.site.register(Image)

admin.site.register(Contact, ContactAdmin)