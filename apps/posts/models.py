from django.db import models

from base.models import BaseModel
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Post(BaseModel):
    author = models.ForeignKey(UserModel, models.CASCADE, null=True)
    text = models.TextField()


class Like(BaseModel):
    author = models.ForeignKey(UserModel, models.CASCADE, null=True)
    post = models.ForeignKey(Post, models.CASCADE, null=True)
    response = models.BooleanField()
