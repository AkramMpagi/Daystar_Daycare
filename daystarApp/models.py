from django.db import models

# Create your models here.

    
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True, default=0)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=200, null=True, blank=True)
    mother_name = models.CharField(max_length=200, null=True, blank=True)
    
    
    
    class Meta:
        verbose_name_plural = "Babies"
    def __str__(self):
        return self.name

    

class Payment(models.Model):
    payee = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    # c_pay = models.ForeignKey(CategoryStay, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    pay_no = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=3, default='Ugx', null=True, blank=True)

    def __str__(self):
        return str(self.payee)
    

class Sitter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, choices=(('Kabalagala','Kabalagala'), ('','')))
    next_of_kin = models.CharField(max_length=100,)
    contact = models.IntegerField(null=True, blank=True)
    nin = models.CharField(max_length=14)
    recommender_name = models.CharField(max_length=100)




    # category = models.ForeignKey(CategoryStay, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=8, choices=(("Full Day","Full Day"), ("Half Day","Half Day")))
    timeIn = models.DateField(null=True, blank=True)
    timeOut = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Doll(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=3, default='Ugx', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    

    

    