from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self):
        return self.username


class Room(models.Model):
    name = models.CharField(max_length=64, blank=True)
    online = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()


class Message(models.Model):
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.text}'
