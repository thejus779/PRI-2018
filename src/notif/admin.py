from django.contrib import admin
from .models import Notification
from .models import Reply

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['message', 'part_id', 'buyer_id', 'is_valid', 'seller_id']


admin.site.register(Notification, NotificationAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['message', 'part_id', 'buyer_id', 'is_accepted', 'seller_id']


admin.site.register(Reply, ReplyAdmin)