from rest_framework.response import Response
from rest_framework import serializers
from .models import Experiment, Variety, Box, CurrentValues

class ExperimentSerializer(serializers.ModelSerializer):
    # current_values = serializers.PrimaryKeyRelatedField(many=True, queryset=CurrentValues.objects.all())
    class Meta:
        model = Experiment
        fields = '__all__'
    
    def create(self, validated_data):
        return Experiment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.max_recurrence = validated_data.get("max_recurrence", instance.max_recurrence)
        instance.max_regime = validated_data.get("max_regime", instance.max_regime)
        instance.max_box_variety = validated_data.get("max_box_variety", instance.max_box_variety)
        instance.start_time = validated_data.get("start_time", instance.start_time)
        instance.save()
        return instance
    
class VarietySerializer(serializers.ModelSerializer):
    # current_values = serializers.PrimaryKeyRelatedField(many=True, queryset=CurrentValues.objects.all())
    class Meta:
        model = Variety
        fields = '__all__'
    
    def create(self, validated_data):
        return Variety.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.sequence_number = validated_data.get("sequence_number", instance.sequence_number)
        instance.is_templated = validated_data.get("is_templated", instance.is_templated)
        instance.sequence_box_number = validated_data.get("sequence_box_number", instance.sequence_box_number)
        instance.relative_template_percent = validated_data.get("relative_template_percent", instance.relative_template_percent)
        instance.score = validated_data.get("score", instance.score)
        instance.additional_info = validated_data.get("additional_info", instance.additional_info)
        instance.save()
        return instance      
        
class BoxSerializer(serializers.ModelSerializer):
    # current_values = serializers.PrimaryKeyRelatedField(many=True, queryset=CurrentValues.objects.all())
    class Meta:
        model = Box
        fields = ['id', 'box_number', 'current_values']
    
    def create(self, validated_data):
        return Box.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.box_number = validated_data.get("box_number", instance.box_number)
        instance.save()
        return instance  
    
class CurrentValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentValues
        fields = '__all__'
    
    def create(self, validated_data):
        # live_plants_temp = validated_data.get("live_plants")
        # all_plants_temp = validated_data.get("all_plants")
        # live_plants_percent_temp =  live_plants_temp / all_plants_temp * 100
        return CurrentValues.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.variety_id = validated_data.get("variety_id", instance.variety_id)
        instance.box_id = validated_data.get("box_id", instance.box_id)
        instance.all_plants = validated_data.get("all_plants", instance.all_plants)
        instance.live_plants = validated_data.get("live_plants", instance.live_plants)
        instance.grown_plants_value = validated_data.get("grown_plants_value", instance.grown_plants_value)
        instance.live_plants_percent = validated_data.get("live_plants") / validated_data.get("all_plants") * 100
        instance.experiment_id = validated_data.get("experiment_id", instance.experiment_id)
        instance.save()
        return instance 