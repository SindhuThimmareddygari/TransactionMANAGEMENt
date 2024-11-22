from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    DEPOSIT = 'DEPOSIT'
    WITHDRAWAL = 'WITHDRAWAL'
    TRANSACTION_TYPES = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal'),
    ]

    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"Transaction {self.id} - {self.transaction_type}"
