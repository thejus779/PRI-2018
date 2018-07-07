from django import forms
from .models import Notification


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
