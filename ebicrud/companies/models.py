from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    email = models.CharField(max_length=100)
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.name

class ServiceOrder(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)

    def __str__(self):
        return self.title

