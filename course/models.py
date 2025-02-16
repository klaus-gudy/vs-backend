from django.db import models
from user.models import User

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('enrolled', 'enrolled'),
        ('pending', 'pending'),
        ('failed', 'failed'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    learner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.learner.username} - {self.course.title}'
