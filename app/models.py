# Create your models here.

from mongoengine import *
from django.contrib.auth.hashers import make_password, check_password


class Pet(Document):
    ANIMAL_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird')
    ]

    pet_id = IntField()
    animal = StringField(choices=ANIMAL_CHOICES)
    breed = StringField(max_length=50)
    climate = StringField(max_length=50)

    def __str__(self):
        return f"{self.pet_id} {self.animal} {self.breed}"


class User(Document):
    name = StringField(max_length=50)
    email = EmailField(unique=True)
    password = StringField(max_length=128)  # Hashed password field

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class UserProfile(Document):
    user = ReferenceField('User', reverse_delete_rule=CASCADE, unique=True)
    favorite_pets = ListField(ReferenceField(Pet))

    def __str__(self):
        return f'{self.user.name}'
