from django.db import models

# Create your models here.


class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True,  null=True)
    body = models.TextField()

    def __str__(self):
        return self.name
