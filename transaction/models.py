from django.db import models
import datetime

# Create your models here.
class record(models.Model):
    name = models.CharField(max_length = 50,default = "", verbose_name= 'ชื่อ')
    date = models.DateField(verbose_name="วันที่", default=datetime.date.today)
    description = models.CharField(max_length = 100,verbose_name="รายละเอียด",default="")
    amountType = [
        ('deposite','deposite'),
        ('withdraw','withdraw'),
        ('transfer','transfer')
    ]
    type = models.CharField(max_length = 15, choices = amountType,default= 'deposite')
    
    amount = models.IntegerField(default=0,verbose_name= 'จำนวนเงิน')



    
    

