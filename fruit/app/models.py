from django.db import models

# Create your models here.
class students(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    mark = models.IntegerField()
    image = models.FileField()