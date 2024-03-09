from django.db import models
from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, blank=True)  
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    option_selected = models.CharField(max_length=100)
    
    
    


    def __str__(self):
        return self.name

