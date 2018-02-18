from django.db import models

# Create your models here.

class coolness(models.Model):
    identifier = models.IntField()
    name = models.CharField(max_length=42)

    class Meta:
        verbose_name = "test"
        ordering = ['id']

    def __str__(self):
        return self.identifier
