import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

def stringUUID():
    return str(uuid.uuid4())


class Basemodel(models.Model):

    id = models.CharField(primary_key=True , default=stringUUID,editable=False , unique=True,max_length = 36)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(  auto_now_add=True)
    

    class Meta:
        abstract = True

class User( AbstractUser ,Basemodel):

    def __str__(self) -> str:
        return self.username

