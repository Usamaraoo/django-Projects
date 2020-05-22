from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Developer(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='images/', default='images/defaultProfile.jpg')
    description_about_u = models.CharField(max_length=1100, blank=False, default='Who ARE YOU')
    skill = models.CharField(max_length=200, default="IT")
    # mail = models.CharField(max_length=200, default='None', blank=False)
    contact_no = models.CharField(max_length=200, default='None', blank=True)

    def get_absolute_url(self):
        return reverse("app:dev_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
