from django.db import models

# Create your models here.

class Customer(models.Model):

    ADDRESS_CHOICES = [
        ('rrg_rahatni', 'RRG Rahatni'),
        ('barclays_office', 'Barclays Office'),
        ('kothrud_depo', 'Kothrud Depo'),
        ('pimple_saudagar', 'Pimple Saudagar'),
        ('Kumar_Picasso', 'Kumar Picasso'),
        ('other', 'Other'),
    ]


    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    kg_ordered = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.full_name