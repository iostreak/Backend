from django.db import models

class contactUs(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=500)

    def __str__(self):
        return self.Name
