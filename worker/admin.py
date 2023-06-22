from django.contrib import admin
from .models import Worker

admin.site.register(Worker)

def __str__(self):
    return self.title