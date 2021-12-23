from django.db import models

# Create your models here.


class FinancialCommitment(models.Model):
    FREQUENCY = (
        ('monthly', 'monthly'),
        ('half-yearly', 'half-yearly'),
        ('yearly', 'yearly'),
        ('single', 'single'),
    )

    CURRENCY = (
        ('PLN', 'PLN'),
        ('CHF', 'CHF'),
        ('EUR', 'EUR'),
        ('USD', 'USD'),
    )

    STATUS = (
        ('open', 'open'),
        ('overdue', 'overdue'),
        ('aborted', 'aborted'),
        ('paid', 'paid'),
    )

    name = models.CharField(max_length=120, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    currency = models.CharField(max_length=3, choices=CURRENCY)
    description = models.TextField(max_length=600, null=True, blank=True)
    date = models.DateField()
    frequency = models.CharField(max_length=11, choices=FREQUENCY)
    status = models.CharField(max_length=7, choices=STATUS)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.amount} {self.frequency}'
