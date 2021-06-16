from django.db import models

class List(models.Model):
    name = models.CharField(max_length=255)

class ListItem(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)