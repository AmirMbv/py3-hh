from django.db import models
from django.contrib.auth.models import User
class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    specialization = models.TextField()
    expected_salary = models.IntegerField (null=True, blank=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author.username

class Resume(models.Model):
    title = models.CharField(max_length=255)
    skillset = models.TextField()
    experience = models.IntegerField(null=True,blank=True)
    workplaces = models.TextField()
    resume = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
