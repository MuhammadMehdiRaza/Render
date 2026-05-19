from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=[
    ("tech","technology"),
    ("edu","Education"),
]

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
