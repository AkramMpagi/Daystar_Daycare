from django.db import models

# Create your models here.
class CategoryStay(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Baby(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    sponsor = models.CharField(max_length=200, null=True, blank=True)
    timeIn = models.DateTimeField(null=True, blank=True)
    timeOut = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Babies"
    def __str__(self):
        return self.name
    
class Sitter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(CategoryStay, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Payment(models.Model):
    payee = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    c_pay = models.ForeignKey(CategoryStay, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    pay_no = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=3, default='Ugx', null=True, blank=True)

    def __int__(self):
        return self.currency