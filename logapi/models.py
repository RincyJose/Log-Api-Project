from django.db import models

# Create your models here.
class log(models.Model):
    msg=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tem  