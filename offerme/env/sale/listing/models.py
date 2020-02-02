from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from resizeimage import resizeimage
from PIL import Image
import random
import string 



CATEGORIES = (
	(0,"Other"),
	(1,"Antique"),
	(2,"Appliances"),
	(3,"Arts & Crafts"),
	(4,"Audio Equipment"),
	(5,"Auto Parts"),
	(6,"Baby & Kids"),
	(7,"Beauty & Health"),
	(8,"Bicycles"),
	(9,"Boats and Marine"),
	(10,"Books & Magazine"),
	(11,"Business Equipment"),
	(12,"Campers & RVs"),
	(13,"Cars & Trucks"),
	(14,"CDs & DVDs"),
	(15,"Cell Phones"),
	(16,"Clothing & Shoes"),
	(17,"Collectables"),
	(18,"Computer Equipment"),
	(19,"Electronics"),
	(20,"Musical Instruments"),
	(21,"TVs"),
	(22,"Video Games"),
	)

CONDITION = (
	(0,"For parts"),
	(1,"Used(normal wear)"),
	(2,"Open Box (never used)"),
	(3,"Reconditioned/Certified"),
	(4,"New(never used)"),
	)

sys_random = random.SystemRandom()

def rand_slug():
    token = ''
    letters = "abcdefghiklmnopqrstuvwwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(1, 9):
        token = token + sys_random.choice(letters)
    return token

class Item(models.Model):
	# Model for item being listed
	title = models.CharField(max_length=350,blank=False)
	image = models.ImageField(upload_to="media/", null=True, blank=False)
	cateogry = models.IntegerField(choices=CATEGORIES, default=0,blank=False)
	condition = models.IntegerField(choices=CONDITION, default=0,blank=False)
	description = models.TextField(max_length=2500,blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2,blank=False,default="0")
	location = models.CharField(max_length=100,blank=False,default="Los Angeles,Ca")
	created_date = models.DateTimeField('date created', default=timezone.now)
	slug = models.SlugField(max_length=8, unique=True, default=rand_slug())
	class Meta:
		ordering = ['-title']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

