from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,firstname,lastname,tel,date_of_birth,city,adress,cni,description,actuelposition,image_url,num_transaction,entreprise_name,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("users must have an username")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            tel = tel,
            date_of_birth = date_of_birth,
            city = city,
            adress = adress,
            cni = cni,
            description = description ,
            actuelposition = actuelposition,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            firstname = "null",
            lastname = "null",
            tel = "null",
            date_of_birth = None,
            city = "null",
            adress = "null",
            cni = "null",
            description = "null" ,
            actuelposition = "null",
            image_url = "null",
            num_transaction = 0,
            entreprise_name = "null",
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.DateTimeField(default=timezone.now,null=True)
    last_login = models.DateTimeField(verbose_name="last login",null=True,auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #password = models.CharField()
    firstname = models.CharField(max_length=30,blank=True,null=True)
    lastname = models.CharField(max_length=30,blank=True,null=True)
    tel =  models.CharField(max_length=30,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    city =  models.CharField(max_length=30,blank=True,null=True)
    adress =  models.CharField(max_length=100,blank=True,null=True)
    cni = models.CharField(max_length=10,blank=True,null=True)
    description = models.CharField(max_length=200,blank=True,null=True)
    actuelposition = models.CharField(max_length=10,blank=True,null=True)
    image_url = models.CharField(max_length=100,blank=True,null=True)
    num_transaction = models.IntegerField(blank=True,null=True)
    entreprise_name = models.CharField(max_length=30,blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
