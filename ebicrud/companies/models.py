from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
