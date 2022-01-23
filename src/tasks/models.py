from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=110)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title