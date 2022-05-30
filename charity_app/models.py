"""
Django models for charity_app.
"""
from django.db import models
from django.contrib.auth.models import User

type_choice = (
    (0, "fundacja"),
    (1, "organizacja pozarządowa"),
    (2, "zbiórka lokalna"),
)

class Category(models.Model):
    name = models.CharField(max_length=64)

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=type_choice, default=0)
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField(null=True)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField(auto_now_add=True)
    pick_up_time = models.TimeField(auto_now_add=True)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # models.DateTimeField
    # datetime.date(1920, 3, 12)
    # datetime.date.today())