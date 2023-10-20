from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    CHOICES = (
        ('.', '...'),
        ('I', 'Info'),
        ('SC', 'Suspension clases'),
        ('SA', 'Suspension actividades'),
    )

    tipo = models.CharField(max_length=5, choices=CHOICES, default='.')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Crear Post"
        