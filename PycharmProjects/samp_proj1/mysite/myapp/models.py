from django.db import models

# Create your models here.

from django.db import models
class Publisher(models.Model):
	name = models.CharField(max_length=30,primary_key=True)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Author(models.Model):
	salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	#headshot = models.ImageField(upload_to='/static')

class Book(models.Model):

	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField()

# Create your models here.
