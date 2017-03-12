from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class libromodelo(models.Model):
    nombre = models.CharField(max_length = 40)
    autor = models.CharField(max_length = 40)
    editorial = models.CharField(max_length = 40)
    ISBN = models.CharField(max_length = 40)
    precio = models.DecimalField(max_digits=9999, decimal_places=2)
    slug = models.SlugField(blank=True)
    tipo = models.CharField(max_length = 40, blank=True, null=True, default="Libro")

    def __unicode__(self):
        return self.nombre

def libros_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = slugify(instance.nombre)

pre_save.connect(libros_pre_save_reciever, sender=libromodelo)