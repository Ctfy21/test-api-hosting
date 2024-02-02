from django.db import models

class Box(models.Model):
    box_number = models.CharField()
    
    def __str__(self):
        return self.box_number

# class Regime(models.Model):
#     title = models.CharField(max_length=100)
#     live_plants_percent_regime = models.FloatField()
    
#     def __str__(self):
#         return self.title

class Variety(models.Model):
    title = models.CharField(max_length=200)
    sequence_number = models.IntegerField(null=True)
    is_templated = models.BooleanField(default=False)
    sequence_box_number = models.PositiveSmallIntegerField()
    relative_template_percent = models.FloatField(null=True)
    score = models.PositiveSmallIntegerField(null=True)
    additional_info = models.TextField(blank=True)
    
    def __str__(self):
        return self.title 


class Experiment(models.Model):
    title = models.CharField(max_length=200)
    max_recurrence = models.PositiveSmallIntegerField()
    max_regime = models.PositiveSmallIntegerField()
    max_box_variety = models.PositiveSmallIntegerField()
    start_time = models.DateField()
     
    def __str__(self):
        return self.title 
  
class CurrentValues(models.Model):
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)
    variety_id = models.ForeignKey(Variety, related_name='current_values', on_delete=models.PROTECT, null = True)
    box_id = models.ForeignKey(Box, related_name='current_values', on_delete=models.PROTECT, null = True)
    # recurrence = models.PositiveSmallIntegerField()
    # regime = models.ForeignKey('Regime', on_delete=models.PROTECT, null = False)
    all_plants = models.PositiveSmallIntegerField()
    live_plants = models.PositiveSmallIntegerField()
    grown_plants_value = models.PositiveSmallIntegerField(null = True)
    live_plants_percent = models.FloatField()
    experiment_id = models.ForeignKey(Experiment, related_name='current_values', on_delete=models.PROTECT, null = True)
    
    def __str__(self):
        return str(self.time_create)

    
