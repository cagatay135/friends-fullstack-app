from django.db import models
from django.db.models.fields import related

# Create your models here.

choices = (
    ('male', 'Male'),
    ('female', 'Female'),
)

class Character(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=choices)
    number_episode = models.PositiveIntegerField()
    most_used_word = models.CharField(max_length=500,null=True,blank=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    portrayed_by = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    image = models.URLField(max_length=200)

    def __str__(self):
        return self.name
        

class Quote (models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='quotes')
    text = models.CharField(max_length=200)
    video = models.URLField(max_length=300, null=True)

    def __str__(self):
        return self.text
