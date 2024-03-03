from django.db import models


class Position(models.Model):
    title=models.CharField(max_length=40)
    def __str__(self):
        return self.title
class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    emp_code = models.CharField(max_length=3)
    mobile=models.CharField(max_length=12)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    

