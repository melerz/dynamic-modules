from django.shortcuts import render
from rest_framework import generics
from eav_app.serializers import *
from eav_app.models import Experiment, Values, Attribute,RawData,Data
from rest_framework import viewsets
# Create your views here.




class ResearcherViewSet(viewsets.ModelViewSet):
	queryset=Researcher.objects.all()
	serializer_class=ResearcherSerializer

class DataViewSet(viewsets.ModelViewSet):
	queryset=Data.objects.all()
	serializer_class=DataSerializer

class DataTypeViewSet(viewsets.ModelViewSet):
	queryset=DataTypes.objects.all()
	serializer_class=DataTypeSerializer

class MethodViewSet(viewsets.ModelViewSet):
	queryset=Methods.objects.all()
	serializer_class=MethodSerializer

class ResearcherViewSet(viewsets.ModelViewSet):
	queryset=Researcher.objects.all()
	serializer_class=ResearcherSerializer




# class ExperimentList(generics.ListCreateAPIView):
# 	queryset = Experiment.objects.all()
# 	serializer_class = ExperimentSerializer

# class ExperimentDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Experiment.objects.all()
# 	serializer_class = ExperimentSerializer

# class ValuesList(generics.ListCreateAPIView):
# 	queryset = Values.objects.all()
# 	serializer_class = ValuesSerializer

# class ValuesDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Values.objects.all()
# 	serializer_class = ValuesSerializer

# class AttributeList(generics.ListCreateAPIView):
# 	queryset = Attribute.objects.all()
# 	serializer_class = AttributeSerializer

# class AttributeDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Attribute.objects.all()
# 	serializer_class = AttributeSerializer

# class RawDataList(generics.ListCreateAPIView):
# 	queryset = Data.objects.all()
# 	serializer_class =  RawDataSerializer

# class RawDataDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = RawData.objects.all()
# 	serializer_class = RawDataSerializer
