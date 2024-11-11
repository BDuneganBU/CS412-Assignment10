from django.db import models

# Create your models here.
class Result(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()