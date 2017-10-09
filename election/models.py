from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=10)
    area = models.CharField(max_length=15)
    introduction = models.TextField()
    party_number = models.IntegerField(default=0)
