from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Experiment, Variety, CurrentValues, Box
from .serializers import ExperimentSerializer, VarietySerializer, BoxSerializer, CurrentValuesSerializer

class ExperimentAPIList(generics.ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

class ExperimentAPIUpdate(generics.UpdateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    
class ExperimentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    
    
class VarietyAPIList(generics.ListCreateAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer

class VarietyAPIUpdate(generics.UpdateAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    
class VarietyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    
    
class BoxAPIList(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxAPIUpdate(generics.UpdateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    
class BoxAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    
    
class CurrentValuesAPIList(generics.ListCreateAPIView):
    queryset = CurrentValues.objects.all()
    serializer_class = CurrentValuesSerializer

class CurrentValuesAPIUpdate(generics.UpdateAPIView):
    queryset = CurrentValues.objects.all()
    serializer_class = CurrentValuesSerializer
    
class CurrentValuesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrentValues.objects.all()
    serializer_class = CurrentValuesSerializer