from django.db import models
from authentication .models import User

# Create your models here.
class Income(models.Model):
    SOURCE_OPTIONS =[
        ('SALARY','SALARY'),
        ('BUSINESS',' BUSINESS'),
        ('SIDE-HUTLES','SIDE-HUTLES'),
        ('OTHERS','OTHERS'),

    ]
    
    source = models.CharField(choices=SOURCE_OPTIONS,max_length=255)
    amount = models.DecimalField(max_digits=10,decimal_places=2,max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    
    class Meta:
        ordering=['-date']

    def __str__(self):
        return (self.owner)+'s income'   