from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GCPInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auth = models.TextField()

    def __str__(self):
        return self.auth