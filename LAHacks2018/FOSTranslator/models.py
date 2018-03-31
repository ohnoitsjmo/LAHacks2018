from django.db import models

# Create your models here.
class Idiom(models.Model):
    idiom = models.CharField(max_length = 400)
    definition = models.CharField(max_length = 1000)

    def __str__(self):
        return self.definition
