from django.db import models

# Create your models here.
class User(models.Model):
    lastname = models.CharField(max_length=264)
    firstname = models.CharField(max_length=264)
    email = models.EmailField(unique=True)

    def __str__(self):
        return ' '.join([self.lastname, self.firstname])