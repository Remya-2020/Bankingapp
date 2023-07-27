from django.db import models

# Create your models here.
class Banking(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phoneno = models.CharField(max_length=15)
    mailid = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    # Use a choice field for accounttype and materials
    accounttype = models.CharField(max_length=20, choices=[('S', 'Savings'), ('C', 'Current'), ('F', 'Fixed')])
    materials = models.CharField(max_length=50,
                                 choices=[('D', 'Debit card'), ('C', 'Credit card'), ('P', 'Cheque book')])
