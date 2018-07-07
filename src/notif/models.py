from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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


class Reply(models.Model):
    is_accepted = models.BooleanField(default=False)
    buyer_id = models.PositiveIntegerField(blank=False)
    seller_id = models.PositiveIntegerField(blank=False)
    part_id = models.PositiveIntegerField(blank=False)
    message = models.CharField(max_length=255, blank=False, help_text='Messagr from seller')

    def __str__(self):
        return self.message
    @property
    def title(self):
        return self.message #objectect.title
    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Reply'


@receiver(pre_save, sender = Notification)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving')

    print(instance)

    # if not instance.slug:
    #         # instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, sender=Notification)