from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name

class Computer_kind(models.Model):
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "computer_kinds"

	def __str__(self):
		return self.name



class Memory(models.Model):
	ram = models.CharField(max_length=100,blank=True,null=True)
	memory_type = models.CharField(max_length=100,blank=True,null=True)
	speed = models.CharField(max_length=100,blank=True,null=True)

class Chipset(models.Model):
	gpu_model = models.CharField(max_length=100,blank=True,null=True)
	gpu_memory_shared = models.CharField(max_length=100,blank=True,null=True)
	hdmi_port = models.BooleanField()

class Audio(models.Model):
	speaker = models.BooleanField()

class Connectivity(models.Model):
	usb_port = models.BooleanField()
	bluetooth = models.CharField(max_length=100,blank=True,null=True)
	digital_media_reader = models.CharField(max_length=100,blank=True,null=True)

class Battery(models.Model):
	battery_type = models.CharField(max_length=100,blank=True,null=True)
	battery_cell = models.CharField(max_length=100,blank=True,null=True)


class Operating_System(models.Model):
	os = models.CharField(max_length=100,blank=True,null=True)

class Dimension(models.Model):
	dimensions = models.CharField(max_length=100,blank=True,null=True)
	weight = models.CharField(max_length=100,blank=True,null=True)

class After_Sale_Service(models.Model):
	warranty = models.CharField(max_length=100,blank=True,null=True)



class Display_Features(models.Model):
	screen_size = models.CharField(max_length=100,blank=True,null=True)
	maximum_display_resolution = models.CharField(max_length=100,blank=True,null=True)
	panel_type = models.CharField(max_length=100,blank=True,null=True)



class Computer_Specification(models.Model):
	processor_description = models.CharField(max_length=100,blank=True,null=True)
	memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
	hard_drive = models.CharField(max_length=100,blank=True,null=True)
	display_features = models.ForeignKey(Display_Features, on_delete=models.CASCADE)
	chipset = models.ForeignKey(Chipset, on_delete=models.CASCADE)
	audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
	connectivity = models.ForeignKey(Connectivity, on_delete=models.CASCADE)
	battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
	operating_systems = models.ForeignKey(Operating_System, on_delete=models.CASCADE)
	dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
	after_sale_service = models.ForeignKey(After_Sale_Service, on_delete=models.CASCADE)




class Computer_Feature(models.Model):
	processor = models.CharField(max_length=100,blank=True,null=True)
	ram = models.CharField(max_length=100,blank=True,null=True)
	inbuilt_hdd = models.CharField(max_length=100,blank=True,null=True)
	os = models.CharField(max_length=100,blank=True,null=True)

class Computer_Brand(models.Model):
	brand_name = models.CharField(max_length=100,blank=True,null=True)
	brand_logo = models.ImageField(upload_to='brand/%Y/%m/%d')


class Computer(models.Model):

	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True,unique=True)
	brand = models.ForeignKey(Computer_Brand, on_delete=models.CASCADE)
	feature = models.ForeignKey(Computer_Feature, on_delete=models.CASCADE)
	specification = models.ForeignKey(Computer_Specification, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='computers/%Y/%m/%d')
	color = models.CharField(max_length=100,blank=True,null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	category = models.ForeignKey(Category,related_name='computers')
	computer_type = models.ForeignKey(Computer_kind,related_name='computers')

	class Meta:
		ordering = ('name',)


	def __str__(self):
		return self.name



	


# user registration models
class UserManager(BaseUserManager):

	def _create_user(self,username, email, password, **extra_fields):
		if not email:
			raise ValueError('User must have email address')

		email = self.normalize_email(email)
		# username = self.normalize_username(username)
		user = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, email, password, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(username, email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(
		_('username'),
		max_length=150,
		blank=True,
		help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
		error_messages={
            'unique': _("A user with that username already exists."),
            },
            )
	email = models.EmailField(_('email address'), unique=True, null=True)
	
	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
		)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
            ),
		)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	# def clean(self):
	# 	super().clean()
	# 	self.email = self.__class__.objects.normalize_email(self.email)

	def get_full_name(self):
		full_name = '%s' % (self.username)
		return full_name.strip()

	def get_short_name(self):
		return self.email

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.email], **kwargs)




