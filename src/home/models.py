from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .validators import validate_category
from .utils import unique_slug_generator
from django.dispatch import receiver
# from sorl.thumbnail import ImageField, get_thumbnail
from django.conf import settings
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=500)
    imageFile = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)


class Parts(models.Model):
    name = models.CharField(max_length=30, blank=True, help_text='Name of your product')
    # category = models.OneToOneField(User, on_delete=models.CASCADE) validators=[validate_category]
    category = models.CharField(max_length=120, null=True, blank=True,validators=[validate_category])
    owner = models.ForeignKey(User)
    # visualQuality = models.CharField(max_length=30, blank=True, help_text='Manufacturer name')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    manufacturer = models.CharField(max_length=30, blank=True, help_text='Manufacturer name')
    modelName = models.CharField(max_length=255, blank=True, help_text='Model name')
    manufacturingYear = models.CharField(max_length=30, blank=True, help_text='Manufacturing year')
    description = models.CharField(max_length=3000, blank=True, help_text='Description about the product')
    usedDuration = models.CharField(max_length=30, blank=True, help_text='Number of years the product is used')
    images = models.FileField(upload_to='images/%Y/%m/%D/', null=True, verbose_name="")
    is_available = models.BooleanField(default=False)

    # email = 		models.EmailField(max_length=255, blank=True,help_text='Required. Inform a valid email address.')
    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name #objectect.title
    class Meta:
        verbose_name = 'Parts'
        verbose_name_plural = 'Parts'

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         self.image = get_thumbnail(self.image, '300x400', quality=99, format='JPEG')
    #     super(Parts, self).save(*args, **kwargs)


@receiver(pre_save, sender=Parts)
def post_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving')
    print(instance)
    print(instance.timestamp)

    instance.category = instance.category.upper()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(post_pre_save_receiver, sender=Parts)

# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()


# pre_save.connect(rl_pre_save_receiver,sender=Parts)

# post_save.connect(rl_post_save_receiver,sender=RestaurantLocation)