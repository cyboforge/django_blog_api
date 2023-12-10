from django.db import models
from django.contrib.auth.models import AbstractUser
from user.helpers import generate_random_username
from django.core.validators import RegexValidator


class User(AbstractUser):
  email = models.CharField(max_length=256, unique=True, null=False, blank=False)
  username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[RegexValidator(
            regex=r'^[\w-]+$',
            message='Username can only contain letters, digits, underscores, and hyphens.',
            code='invalid_username'
        )]
    )
  REQUIRED_FIELDS = ['password']

  def save(self, *args, **kwargs):
    if not self.username:
      self.username = generate_random_username()

  def __str__(self):
    return self.email