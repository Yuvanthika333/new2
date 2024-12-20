from django.db import models

# Create your models here.
class Students(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    cpass=models.CharField(max_length=50)
    

    class Meta:
        db_table="tbl_students"

class Stud(models.Model):
    stud_name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    con_password=models.CharField(max_length=100)
    student_c=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table="tbl_student"

   