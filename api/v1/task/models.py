from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class File(models.Model):
    GROUP_CHOICES = [
        ('Media', 'Media'),
        ('Docs', 'Docs'),
        ('Videos', 'Videos'),
    ]
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='author_files',
    )
    sharing = models.ManyToManyField(
        User,
        related_name='sharing_files',
        blank=True,
    )
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='files/')
    group = models.CharField(max_length=128, choices=GROUP_CHOICES, default='Docs')

    def __str__(self):
        return self.name
