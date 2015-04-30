from django.db import models
from django_hstore import hstore
# E-A-V

#Attribute
class Attribute(models.Model):
	name   			= models.CharField(primary_key=True,max_length=100)
	description   	= models.CharField(max_length=100,blank=True)

	def __unicode__(self):
		return self.name

#Entity / Object
class Experiment(models.Model):
	name = models.CharField(primary_key=True,max_length=100)
	def __unicode__(self):
		return self.name

#Value
class Values(models.Model):
	experiments = models.ManyToManyField(Experiment,related_name='fields')
	attribute = models.ForeignKey('Attribute',related_name='values')

	def __unicode__(self):
		return self.attribute.name

## give me all experiments tha have fields with value "d"
#>>> Experiment.objects.filter(values__value__startswith="d")
#<Experiment: exp1>, <Experiment: exp2>] 

class RawData(models.Model):
	name = models.CharField(max_length=32)
	data = hstore.DictionaryField()
	objects = hstore.HStoreManager()

class Data(models.Model):
	name=models.CharField(primary_key=True,max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	researcher = models.ForeignKey('Researcher',related_name='data_generated')
	isRawData = models.BooleanField(default='true')
	dataType = models.ForeignKey('DataTypes',related_name='data')
	source = models.ForeignKey('self',null=True,blank=True,related_name='data_generated') 
									   #analyze result can come from device or
									   #an intermidiate data like fastq 
	description=models.CharField(max_length=400,blank='true')
	#method = models.ForeignKey('Methods',related_name='output')
	attributes = hstore.DictionaryField()
	objects = hstore.HStoreManager()

	def __unicode__(self):
		return unicode(self.name)

class Researcher(models.Model):
	name=models.CharField(primary_key=True,max_length=200)
	attributes = hstore.DictionaryField()
	objects = hstore.HStoreManager()

	def __unicode__(self):
		return unicode(self.name)

class Methods(models.Model):
	name=models.CharField(primary_key=True,max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	researcher = models.ForeignKey('Researcher',related_name='methods')
	description=models.CharField(max_length=400)
	dataType = models.ForeignKey('DataTypes',related_name='methods')
	attributes = hstore.DictionaryField()
	objects = hstore.HStoreManager()

	def __unicode__(self):
		return unicode(self.name)


class DataTypes(models.Model):
	name=models.CharField(primary_key=True,max_length=200)

	def __unicode__(self):
		return unicode(self.name)


    # data = hstore.DictionaryField(schema=[
    #     {
    #         'name': 'description',
    #         'class': 'CharField',
    #         'kwargs': {
    #             'default': 'test author',
    #             'max_length':100
    #         }
    #     },
    #     {
    #         'name': 'author',
    #         'class': 'CharField',
    #         'kwargs': {
    #             'default': 'test author',
    #             'max_length':100
    #         }
    #     }]
    #  )  # can pass attributes like null, blank, etc.