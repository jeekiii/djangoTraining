from django.db import models

# Create your models here.

class Coolness(models.Model):
    identifier = models.IntegerField()
    name = models.CharField(max_length=42)
    class Meta:
        verbose_name = "test"
        ordering = ['identifier']

    def __str__(self):
        return str(self.identifier)

class Member(models.Model):
    name = models.CharField(max_length=42)
    group = models.ForeignKey('Coolness', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
