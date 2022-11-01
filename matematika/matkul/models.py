from pyexpat import model
from django.db import models

# Create your models here.
class Matkul(models.Model):
    no = models.CharField(max_length=200)
    kode = models.CharField(max_length=200)
    mata_kuliah = models.CharField(max_length=200)
    wp = models.CharField(max_length=200)
    sks = models.CharField(max_length=200)