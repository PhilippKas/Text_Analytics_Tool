from django.db import models

# Create your models here.
class Comments(models.Model):
    comment = models.CharField(max_length = 1000)
    tool = models.CharField(max_length = 50)
    published_date = models.DateField()