from django.db import models

# Create your models here.


class PersonModel(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
