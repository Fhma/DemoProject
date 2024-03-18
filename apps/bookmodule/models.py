from django.db import models

class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    edition = models.SmallIntegerField()
    
class Publish(models.Model):
    address = models.CharField()
    
