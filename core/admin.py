from django.contrib import admin
from .models import Vacancy, Company

admin.site.register(Vacancy)
admin.site.register(Company)

def __str__(self):
    return self.title