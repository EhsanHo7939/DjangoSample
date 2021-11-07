from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name="Authorship Status")
    VIP_user = models.DateTimeField(default=timezone.now, verbose_name="VIP until")

    def is_VIP_user(self):
        if self.VIP_user >= timezone.now():
            return True
        else:
            return False
    
    is_VIP_user.boolean = True
    is_VIP_user.short_description = "VIP Status"