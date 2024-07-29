from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    cash = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    participants = models.JSONField(default=list, blank=True)

    def __str__(self) -> str:
        return self.user.name