from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class AddCash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    source = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"{self.user.username} - {self.source} - {self.amount}"
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"{self.user.username} - {self.amount}"
    

