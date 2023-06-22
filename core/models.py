from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')

class Company(models.Model):
    title = models.CharField(max_length=255)
    address = models.TextField()
    employees_number = models.IntegerField(null=True, blank=True)
    is_hunting = models.BooleanField(default=True)