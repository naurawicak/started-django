import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Pertanyaan(models.Model):
    pertanyaan_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pertanyaan_text
    
    def was_publish_terbaru(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Pilih(models.Model):
    pertanyaan= models.ForeignKey(Pertanyaan, on_delete=models.CASCADE)
    pilih_text = models.CharField(max_length=200)
    suara = models.IntegerField(default=0)

    def __str__(self):
        return self.pilih_text
    
    


