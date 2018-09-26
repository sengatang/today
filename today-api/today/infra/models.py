from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nick_name = models.CharField()
    last_name = models.CharField()
    open_id = models.CharField()
    union_id = models.CharField()
    mini_openid = models.CharField()

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.CharField()
    is_finished = models.BooleanField(default=False) # 表示是否完成
    is_active = models.BooleanField(default=True) # 用于归档 Archive

class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField()
    description = models.CharField()
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    manager = models.ManyToManyField(User)

