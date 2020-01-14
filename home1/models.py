
from django.db import models
from datetime import datetime




class PatientRegstration(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=200)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    Gender_choices = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=Gender_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    patient_type = models.CharField(max_length=200)
    age = models.IntegerField()
    # def super(). __init__(self):
    #     return self.patient_id
    def __str__(self):
        return self.patient_name
    # def male(self):
    #     return self.filter(gender=self.GENDER_MALE)
    # def female(self):
    #     return self.filter(gender=self.GENDER_FEMALE)
    def currentTimestamp(self):
        return self.created_at
    def patientType(self):
        return self.patient_type
