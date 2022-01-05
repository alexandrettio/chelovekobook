from django.db import models

# Create your models here.
from django.db.models import TextField, CharField, ImageField


class Profile(models.Model):
    full_name = CharField(max_length=100)
    photo = ImageField()
    about = TextField()
