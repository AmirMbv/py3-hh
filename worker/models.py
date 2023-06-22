from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.TextField()
    expected_salary = models.IntegerField (null=True, blank=True)
    is_searing = models.BooleanField(default=True)
