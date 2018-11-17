from django.contrib.auth.models import AbstractUser


class FinUser(AbstractUser):
    def __str__(self):
        return self.email
