from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

choise=[
    ("Male","Male"),
    ("Female","Female")
]

class Patient_detail(models.Model):
    name            = models.CharField(max_length=100)
    age             = models.IntegerField()
    gender          = models.CharField(choices=choise,max_length=50,default='Male')
    mobile_number   = PhoneNumberField(unique=True,default='+91')
    procedure       = models.CharField(max_length=300)
    date            = models.DateField(default=datetime.date.today)
    time            = models.DateTimeField(auto_now_add=True)
    reffered_by     = models.CharField(max_length=100,blank=True,null=True)
    comment         = models.CharField(max_length=300,blank=True,null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-time']

    



