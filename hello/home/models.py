from django.db import models

class Contact(models.Model): # this is a database
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
# Create your models here.
