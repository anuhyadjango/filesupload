from django.db import models

# Create your models here.
class profiles(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    tech = models.CharField(max_length=40)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(default = None)
    photo = models.FileField()
    class Meta:
        db_table = 'profiles'
