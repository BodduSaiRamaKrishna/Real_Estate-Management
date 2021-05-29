from django.db import models

# Create your models here.
class Details(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    email=models.CharField(max_length=50,null=True)
    fname=models.CharField(max_length=30,null=True)
    lname=models.CharField(max_length=50,null=True)
    num=models.IntegerField(max_length=10,null=True)
    add=models.CharField(max_length=80,null=True)
    pin=models.CharField(max_length=10,null=True)
    state=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.lname

class Feedback(models.Model):
    fname=models.CharField(max_length=30,null=True)
    lname=models.CharField(max_length=30,null=True)
    country=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.lname


class Image(models.Model):
    objects = None
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption

class Tran(models.Model):
    fname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    add=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=30,null=True)
    state=models.CharField(max_length=30,null=True)
    zip=models.CharField(max_length=10,null=True)
    cname=models.CharField(max_length=30,null=True)
    cnum=models.CharField(max_length=12,null=True)
    expmonth=models.CharField(max_length=2,null=True)
    expyear=models.CharField(max_length=4,null=True)
    cvv=models.CharField(max_length=3,null=True)


    def __str__(self):
        return self.fname
