from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(verbose_name='titre')
    text = model
