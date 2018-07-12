from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from core.models import User
from core.models import Profile
from home.models import Parts
from django.contrib import messages
# Create your models here.


class Notification(models.Model):
    is_valid = models.BooleanField(default=False)
    buyer_id = models.PositiveIntegerField(blank=False)
    seller_id = models.PositiveIntegerField(blank=False)
    part_id = models.PositiveIntegerField(blank=False)
    message = models.CharField(max_length=255, blank=False, help_text='Message for user about notification')
    buyer_name = models.CharField(max_length=30, blank=True, help_text='Full name.')
    part_name = models.CharField(max_length=30, blank=True, help_text='Name of your product')

    def __str__(self):
        return self.message
    @property
    def title(self):
        return self.message #objectect.title
    class Meta:
        verbose_name = 'Notifications'
        verbose_name_plural = 'Notifications'


@receiver(pre_save, sender = Notification)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving')

    print(instance)

    # if not instance.slug:
    #         # instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, sender=Notification)

@receiver(post_save, sender = Notification)
def post_save_receiver(sender, instance, *args, **kwargs):

    if instance.is_valid:
        seller = User.objects.get(id=instance.seller_id);
        buyer = User.objects.get(id=instance.buyer_id);
        part = Parts.objects.get(id=instance.part_id);

        subject = 'Exchange requested for ' + part.name
        body = 'The product ' + part.name + ' by ' + part.manufacturer + ' has been requested to be exchanged . You can reply back by clicking this link' + 'http://127.0.0.1:8000/reply/%s' % (
            instance.buyer_id)

        email = EmailMessage(subject, body, to=[seller.email])
        email.send()

    # if not instance.slug:
    #         # instance.slug = unique_slug_generator(instance)


post_save.connect(post_save_receiver, sender=Notification)


class Reply(models.Model):
    is_accepted = models.BooleanField(default=False)
    buyer_id = models.PositiveIntegerField(blank=False)
    seller_id = models.PositiveIntegerField(blank=False)
    part_id = models.PositiveIntegerField(blank=False)
    exchange_part_id = models.PositiveIntegerField(blank=False)
    message = models.CharField(max_length=255, blank=False, help_text='Message from seller')

    def __str__(self):
        return self.message
    @property
    def title(self):
        return self.message #objectect.title
    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Reply'


@receiver(post_save, sender = Reply)
def post_save_receiver(sender, instance, *args, **kwargs):

    seller = User.objects.get(id=instance.seller_id);
    buyer = User.objects.get(id=instance.buyer_id);
    part = Parts.objects.get(id=instance.part_id);

    profileSeller = Profile.objects.get(user=seller);

    subject = 'Exchange request accepted' + part.name

    if(instance.exchange_part_id == 0):
        body = 'Exchange request for ' + part.name + ' Accepted  for FREE. ' + 'Personal Message: ' + instance.message + '. Email :' + seller.email + ' Mobile:' + profileSeller.mobilenumber
        print('mail sent free')
    else:
        exchange_part = Parts.objects.get(id=instance.exchange_part_id);
        body = 'Exchange request for ' + part.name + ' Accepted. The user would like to exchange it with' + exchange_part.name + '. Personal Message: ' + instance.message + ' Email :' + seller.email + ' Mobile:' + profileSeller.mobilenumber
        print('mail sent')
    email = EmailMessage(subject, body, to=[buyer.email])
    email.send()

    # if not instance.slug:
    #         # instance.slug = unique_slug_generator(instance)


post_save.connect(post_save_receiver, sender=Reply)
