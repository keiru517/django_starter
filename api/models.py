from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your models here.
class Document(models.Model):
    category = models.CharField(default="", max_length=50)

    def upload_path(self, filename):
        return f'documents/{self.category}/{filename}'
    
    file = models.FileField(upload_to=upload_path)
    name = models.CharField(default="", max_length=100)
    size = models.CharField(default="", max_length=10)
    description = models.CharField(default="", max_length=50)
    created_at = models.DateTimeField(default=datetime.now)

    
