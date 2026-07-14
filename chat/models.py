from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=200)

    created=models.DateTimeField(auto_now_add=True)

class Message(models.Model):

    thread=models.ForeignKey(
    Thread,
    related_name="messages",
    on_delete=models.CASCADE
)

    role=models.CharField(max_length=20)

    content=models.TextField()

    created=models.DateTimeField(auto_now_add=True)