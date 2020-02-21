from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    cover_pics = models.ImageField(default='default.jpg', upload_to='cover_pics')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
