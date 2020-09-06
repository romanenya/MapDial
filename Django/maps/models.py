from django.db import models

# Create your models here.
class Points(models.Model):
	name = models.CharField(max_length=100)
	text = models.TextField()
	point_x = models.IntegerField()
	point_y = models.IntegerField()
	author = models.CharField(max_length=100)
	groop = models.CharField(max_length=100)

	def __str__(self):
		return self.name
	

class Groops(models.Model):
	name = models.CharField(max_length=100)
	about = models.TextField()
	creator = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name