from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your models here.
class Document(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # def upload_path(self, filename):
    #     return f'{self.user.id}/{filename}'
    file = models.FileField(upload_to='')
    name = models.CharField(default="", max_length=100)
    size = models.CharField(default="", max_length=10)
    description = models.CharField(default="", max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    
