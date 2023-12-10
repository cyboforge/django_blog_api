from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  email = models.CharField(max_length=256, unique=True, null=False, blank=False)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.email