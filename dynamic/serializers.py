from rest_framework import serializers
from eav.models import Experiment,Values,Attribute


class ExperimentSerializer(serializers.ModelSerializer):
	#analyzes = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='analyze-detail')
	class Meta:
		model = Experiment
		#fields = ('id','experiments','attribute','value')
		fields = ('name', 'bla')

class ValuesSerializer(serializers.HyperlinkedModelSerializer):
	#created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
	#job = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='job-detail')
	class Meta:
		model = Values
		fields = ('id','experiments','attribute','value')


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
	#created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
	class Meta:
		model = Attribute
		fields = ('name','description')