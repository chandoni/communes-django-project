from django.db import models
from django.contrib.auth.models import User

class Bulletin(models.Model):
    title = models.CharField(max_length=64)
    caption = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Community(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class CommunityMembers(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    members = models.ForeignKey(User, on_delete=models.CASCADE)

class CommunityBulletins(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    bulletins = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
