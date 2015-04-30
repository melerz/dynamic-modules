from rest_framework import serializers
from eav_app.models import *
# rest_framework_hstore
from rest_framework_hstore.fields import HStoreField

class DataSerializer(serializers.HyperlinkedModelSerializer):
	attributes = HStoreField()
	data_generated = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='data-detail')
	class Meta:
		model = Data
		fields = ('name','attributes','researcher','description','dataType','isRawData','created','source','data_generated')

class DataTypeSerializer(serializers.HyperlinkedModelSerializer):
	methods = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='methods-detail')
	data = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='data-detail')
 	class Meta:
 		model = DataTypes
 		fields = ('name','methods','data')

class ResearcherSerializer(serializers.HyperlinkedModelSerializer):
	attributes = HStoreField()
	data_generated = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='data-detail')
	methods = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='methods-detail')
	class Meta:
		model = Researcher
		fields=('name','attributes','data_generated','methods')

class MethodSerializer(serializers.HyperlinkedModelSerializer):
	attributes = HStoreField()
	#output = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='data-detail')
	class Meta:
		model = Methods
		fields = ('name','created','researcher','description','dataType','attributes')


# class AttributeSerializer(serializers.HyperlinkedModelSerializer):
# 	#created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
# 	class Meta:
# 		model = Attribute
# 		fields = ('name','description')


# class RawDataSerializer(serializers.ModelSerializer):
#     attributes = HStoreField()
#     class Meta:
#         model = Data
#         fields = ('name','attributes','researcher','description','dataType','isRawData','created')

# class ExperimentSerializer(serializers.ModelSerializer):
# 	#values = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='value-detail')
# 	fields = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='values-detail')
# 	class Meta:
# 		model = Experiment
# 		fields = ('name','fields')

# class ValuesSerializer(serializers.HyperlinkedModelSerializer):
# 	#created = serializers.DateTimeField(format='%Y-%m-%d-%H:%M',read_only=True)
# 	#job = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='job-detail')
# 	class Meta:
# 		model = Values
# 		fields = ('id','experiments','attribute','value')