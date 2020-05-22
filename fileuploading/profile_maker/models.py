from django.db import models


# Create your models here.
class User_Profile(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    technologies = models.CharField(max_length=200)
    email = models.EmailField()
    display_picture = models.FileField()

    def __str__(self):
        return self.fname
