from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  first_name = models.TextField(blank=True)
  last_name = models.TextField(blank=True)
  work = models.TextField(blank=True)
  relationship = models.TextField(blank=True)
  bio = models.TextField(blank=True)
  profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
  location = models.CharField(blank=True, max_length=100)
  
  def __str__(self):
    return self.user.username