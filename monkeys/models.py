from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class MonkeyProfile(models.Model):
	user = models.OneToOneField(User)

	#additional attribiutes of the Monkey
	age = models.PositiveIntegerField()
	picture = models.ImageField(upload_to='profile_images', blank=True)
	

	#return the username
	def __unicode__(self):
		return self.user.username
