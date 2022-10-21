from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)