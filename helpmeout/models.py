from django.db import models

# Create your models here.

class AccessToken(models.Model):
    oauth_token = models.CharField(max_length=100000)
    ot_secret = models.CharField(max_length=100000)
    user_id = models.CharField(max_length=100000)
    screen_name = models.CharField(max_length=100000)
