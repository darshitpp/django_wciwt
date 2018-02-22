from django.db import models

class Tofetch(models.Model):
    url = models.CharField(max_length=6)