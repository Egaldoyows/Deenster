from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Desination(models.Model):
    des_name = models.CharField(max_length=30)
    cover_image = models.ImageField(upload_to="img/", blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.des_name
    





class Hotel(models.Model):
    cover_image=models.ImageField(upload_to="img/", blank=True)
    name = models.CharField(max_length=30)
    dest_id =models.ForeignKey(Desination,on_delete=models.CASCADE)
    desc = models.TextField()
    

    def __str__(self):
        return str(self.name)
    

    
class Activity(models.Model):
    activity_name= models.CharField(max_length=50)
    activity_desc=models.TextField()
    
    
    def __str__(self) :
        
        return self.activity_name
    

class Addon(models.Model):
    addon= models.CharField(max_length=200,blank=True)
    
    

    def __str__(self) :
        
        return self.addon
    
class Excluded(models.Model):
    addon= models.CharField(max_length=200,blank=True)
    
    

    def __str__(self) :
        
        return self.addon




class Package(models.Model):
    cover_image=models.ImageField(upload_to="img/", blank=True)
    description=models.CharField(max_length=1000)
    name= models.ForeignKey(Hotel,on_delete=models.CASCADE, related_name='package')
    start_date = models.DateField()
    end_date = models.DateField()
    created=models.DateTimeField(auto_now_add=True)
    addons=models.ManyToManyField(Addon,default=None, blank=True)
    excluded=models.ManyToManyField(Excluded,default=None, blank=True)
    activities=models.ManyToManyField(Activity,default=None, blank=True)
    cruiser_price=models.IntegerField()
    van_price=models.IntegerField()
    



    def __str__(self) :
        
        return f"{self.name}-{self.description}"
    

DAYS=[
    (1,'DAY 1'),
    (2,'DAY 2'),
    (3,'DAY 3'),
    (4,'DAY 4'),
    (5,'DAY 5'),
    (6,'DAY 6'),
]
    



class TourSchedule(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='schedule')
    days=models.IntegerField(max_length=30, choices=DAYS, default=1)
    activities = models.ManyToManyField(Activity, blank=True)

    def __str__(self):
        return f"{self.package.name}- Day {self.days}"
    












    



NATIONALITY=[
    ('RESIDENT','Resident'),
    ('NON-RESIDENT','Non-Resident')
]



class Tour(models.Model):
    
    full_name= models.CharField(max_length=50)
    email=models.EmailField()
    identity_number=models.CharField(max_length=12)
    phone_number=models.CharField(max_length=12)
    naitionality= models.CharField(max_length=30, choices=NATIONALITY, default='Resident')
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    number=models.PositiveBigIntegerField(default=1)
    price=models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    book_status = models.BooleanField(default=False)
    reject_status = models.BooleanField(default=False)
    reject_reason=models.TextField(blank=True)
    updated_on=models.DateTimeField(auto_now=True)
    

    def __str__(self) :
        
        return str(self.full_name)
    



class EmailTemplate(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=200)

    def __str__(self) :
        
        return str(self.name)






    
    
    




    


    


    




