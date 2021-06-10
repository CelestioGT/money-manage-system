from django.conf import settings
from django.db import models
import datetime
from django.contrib import admin

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
    slug = models.SlugField(null=True, blank=True)
    amount = models.IntegerField(default=0,verbose_name= 'จำนวนเงิน')
    evidence = models.FileField(upload_to='evidence/',null = True, blank = True, verbose_name="หลักฐาน")

class AllTeam(models.Model):   
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50,default = "", verbose_name='ชื่อทีม')
    create_by = settings.AUTH_USER_MODEL
    slug = models.SlugField(null=True, blank=True)
    # date_build = models.DateField(verbose_name="วันที่สร้างทีม", default=datetime.date.today)      

class MyTeam(models.Model):
    team_id = models.IntegerField()
    # date_join = models.DateField(verbose_name="วันที่เข้าร่วมทีม", default=datetime.date.today)
    permissions = models.CharField(max_length = 50,default = "", verbose_name= 'สิทธิ์')

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)   



    
    

