# Create your models here.

from mongoengine import *
from django.contrib.auth.hashers import make_password


class Pet(Document):
    BREED_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird')
    ]

    name = StringField(max_length=50)
    breed = StringField(choices=BREED_CHOICES)
    climate = StringField(max_length=50)

    def __str__(self):
        return self.name


class User(Document):
    name = StringField(max_length=50)
    email = EmailField(unique=True)
    password = StringField(max_length=128)  # Hashed password field

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()


class UserProfile(Document):
    user = ReferenceField('User', reverse_delete_rule=CASCADE)
    favorite_pets = ListField(ReferenceField(Pet))

    def __str__(self):
        return f'{self.user.name}'
