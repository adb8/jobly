from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.first_name + " " + self.last_name
      
# class Job(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     company = models.CharField(max_length=100)
#     description = models.TextField()
#     location = models.CharField(max_length=100)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=100)
#     nextStep = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     skills = ArrayField(models.CharField(max_length=100), blank=True, default=list)
#     during = models.CharField(max_length=100)
#     type = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.title + " at " + self.company
