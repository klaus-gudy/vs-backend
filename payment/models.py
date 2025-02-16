from django.db import models
from course.models import Enrollment

class Payment(models.Model):
    PROVIDER_CHOICES = [
        ('Airtel', 'Airtel'),
        ('Tigo', 'Tigo'),
        ('Halopesa', 'Halopesa'),
        ('Mpesa', 'Mpesa'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='TZS')
    provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES)
    transaction_id = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    paid_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.enrollment.learner.username} - {self.amount} {self.currency} ({self.status})"
