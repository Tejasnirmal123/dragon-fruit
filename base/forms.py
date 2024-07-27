from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    ADDRESS_CHOICES = [
        ('rrg_rahatni', 'RRG Rahatni'),
        ('barclays_office', 'Barclays Office'),
        ('kothrud_depo', 'Kothrud Depo'),
        ('pimple_saudagar', 'Pimple Saudagar'),
        ('Kumar_Picasso', 'Kumar Picasso'),
        ('other', 'Other'),
    ]

    address = forms.ChoiceField(choices=ADDRESS_CHOICES, required=True)
    other_address = forms.CharField(required=False)

    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'contact_no', 'address','landmark','kg_ordered']