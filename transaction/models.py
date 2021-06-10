from django.conf import settings
from django.db import models
import datetime
from django.contrib import admin
from django.contrib.auth.models import User

class AllTeam(models.Model):   
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50,default = "", verbose_name='ชื่อทีม')
    # create_by = models.ForeignKey(User, on_delete=models.CASCADE,default=None, null=True)
    slug = models.SlugField(null=True, blank=True)
    # date_build = models.DateField(verbose_name="วันที่สร้างทีม", default=datetime.date.today) 
    def __str__(self):
        return self.name

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
    evidence = models.FileField(upload_to='evidence/',null = True, blank = True, verbose_name="หลักฐาน")
    team = models.ForeignKey(AllTeam, on_delete=models.CASCADE,default=None, null=True)
     

class MyTeam(models.Model):
    # team_id = models.IntegerField()
    # date_join = models.DateField(verbose_name="วันที่เข้าร่วมทีม", default=datetime.date.today)
    Member = models.ForeignKey(User, on_delete=models.CASCADE,default=None, null=True)    
    team = models.ForeignKey(AllTeam, on_delete=models.CASCADE,default=None, null=True)    
    permissionChoice = [
        ('admin','admin'),
        ('member','member')
    ]
    permissions = models.CharField(max_length = 10,choices = permissionChoice, verbose_name= 'สิทธิ์')


    
    

