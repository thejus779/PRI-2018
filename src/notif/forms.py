from django import forms
from .models import Notification,Reply


class BuyRequest(forms.ModelForm):
    class Meta:
        model = Notification
        fields = [
            'is_valid',
            'buyer_id',
            'part_id',
            'message',
            'seller_id',
            'part_name',
            'buyer_name',
        ]

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'is_accepted',
            'buyer_id',
            'part_id',
            'message',
            'seller_id',
            'exchange_part_id',
        ]
