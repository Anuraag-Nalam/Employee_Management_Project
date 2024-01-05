from django.db import models
class Addemp(models.Model):
    yourid=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100,null=True)
    lastname=models.CharField(max_length=100,null=True)
    male=models.CharField(max_length=100,null=True)
    female=models.CharField(max_length=100,null=True)
    other=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=1000,null=True)
    pancard=models.CharField(max_length=100,null=True)
    salary=models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    number=models.CharField(max_length=100,null=True)
    def __str__(self):
         return self.firstname

# Create your models here.
