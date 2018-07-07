from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator

from django.dispatch import receiver

class Profile(models.Model):
    user = 			models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp =     models.DateTimeField(auto_now_add=True)
    updated =       models.DateTimeField(auto_now=True)
    slug  =         models.SlugField(null=True, blank=True)
    fullname = 		models.CharField(max_length=30, blank=True, help_text='Full name.')
    address =		models.CharField(max_length=255, blank=True, help_text='House number and street')
    city = 			models.CharField(max_length=30, blank=True, help_text='Optional.')
    postalcode = 	models.CharField(max_length=10, blank=True, help_text='Optional.')
    country = 		models.CharField(max_length=30, blank=True, help_text='Optional.')
    mobilenumber = 	models.CharField(max_length=30,blank=True, help_text='Optional.')
    # email = 		models.EmailField(max_length=255, blank=True,help_text='Required. Inform a valid email address.')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("profile create lala")
    print(instance)
    if created:
        Profile.objects.create(user=instance)
        print("profile create")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print("profile saved")


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)