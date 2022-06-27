from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Role(models.Model):
    Role = models.CharField(max_length=15)
    class Meta:
        db_table = 'role'
        # verbose_name_plural='role'
    
    def __str__(self) -> str:
        return self.Role


class Del_Status(models.Model):
    Del_Status = models.CharField(max_length=15)
    class Meta:
        db_table = 'del_Status'
        # verbose_name_plural='role'
    
    def __str__(self) -> str:
        return self.Del_Status

class Shop_Types(models.Model):
    Shop_Types = models.CharField(max_length=15)
    class Meta:
        db_table = 'shop_types'
        verbose_name_plural='shop_types'
    
    def __str__(self) -> str:
        return self.Shop_Types

class Master(models.Model):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Email = models.EmailField(max_length=25, unique=True)
    Password = models.CharField(max_length=15)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'
        # verbose_name_plural='master'
    
    # def __str__(self) -> str:
    #     return self.Master

del_choices=(
    ('y','yes'),
    ('n','no'),
    )

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
    )

class Profile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    
    
    # CUSTOMER FIELDS
    ProfileImage = models.FileField(upload_to="images/users", default="")
    First_Name = models.CharField(max_length=25, default="")
    Last_Name = models.CharField(max_length=25, default="")
    DOB = models.DateField(auto_created=True, default="2020-01-01")
    Gender = models.CharField(max_length=10, choices=gender_choices)

    #  Shop Basic Details 
    
    # ShopImage = models.FileField(upload_to="images/shops", default="images/shop.png")
    OwnerName = models.CharField(max_length=25, default="")
    ShopName = models.CharField(max_length=25, default="")
    Del_Status = models.ForeignKey(Del_Status,on_delete=models.CASCADE,default='2')
    

    # Foreign 
    Shop_Types = models.ForeignKey(Shop_Types, on_delete=models.CASCADE,default='1')
    
    DOJ = models.DateField(auto_now=True) # Date of Joining from Near.in Organisation
    DOS = models.DateField(auto_created=True, default="2020-01-01") # Date of Started

    

    #Contact/ Address
    Contact = models.CharField(max_length=12, default="")
    # H_S_no = models.CharField(max_length=25, default="")
    # Complex_Name = models.CharField(max_length=25, default="")
    # Nr_Landmark = models.CharField(max_length=25, default="")
    Country = models.CharField(max_length=25, default="")
    City = models.CharField(max_length=25, default="")
    State = models.CharField(max_length=25, default="")
    Pincode = models.CharField(max_length=25, default="")
    Address = models.TextField(max_length=250, default="")

    class Meta:
        db_table = 'profile'
    
    # def __str__(self) -> str:
    #     return self.Profile