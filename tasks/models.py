from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Basse', 'Basse'),
        ('Moyenne', 'Moyenne'),
        ('Haute', 'Haute'),
    ]

    CATEGORY_CHOICES = [
        ('Études', 'Études'),
        ('Travail', 'Travail'),
        ('Personnel', 'Personnel'),
        ('Autre', 'Autre'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Moyenne')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Autre')

    def __str__(self):
        return self.title