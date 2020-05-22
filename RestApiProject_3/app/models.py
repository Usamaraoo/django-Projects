from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=20)
    skills = models.CharField(max_length=550)
    about_you = models.CharField(max_length=600)

    def __str__(self):
     return self.name