from django.db import models

class Kouka2(models.Model):
    product = models.CharField(max_length=1000)
    area = models.CharField(max_length=1000)
    delivery = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    attachment = models.CharField(max_length=1000)

    def __str__(self):
        return self.product + ' / ' + self.area