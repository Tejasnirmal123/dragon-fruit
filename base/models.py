from django.db import models

# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    address = models.TextField()
    kg_ordered = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.full_name