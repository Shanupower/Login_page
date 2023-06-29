from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser, PermissionsMixin):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name              = models.CharField(max_length=60, blank=True, null=True)
	last_name               = models.CharField(max_length=60, blank=True, null=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	last_ip_address			= models.GenericIPAddressField(null=True, blank=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	objects = MyAccountManager()

	def __str__(self):
		return self.email

class UserModel(models.Model):
	name = models.CharField(max_length=100)
	emailId = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
    
	def __str__(self):
	    return self.email

class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    core_categories = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')