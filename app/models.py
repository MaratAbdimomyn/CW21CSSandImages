from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=40)
    model_name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to='images')