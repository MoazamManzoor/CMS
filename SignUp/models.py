from django.db import models

 #Create your models here.

class Teacher_info(models.Model):
    t_id=models.CharField(max_length=13,primary_key=True,default=0,editable=False)
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id=models.EmailField()
