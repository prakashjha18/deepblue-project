
from django.db import models
from datetime import datetime



class DoctorInfo(models.Model):
    D_name = models.CharField(max_length=200)
    D_username = models.CharField(max_length=200,unique=True)
    D_email = models.EmailField(max_length=254,unique=True)
    Domain_choices = [(1, 'Primary Health Care'), (2, 'Pediatric Clinic'), (3, 'Gynaecological Clinic'), (4, 'Outpatient Surgery')]
    domain = models.IntegerField(choices = Domain_choices)
    choice = [(0, 'YES'), (1, 'NO')]
    isavail = models.IntegerField(choices = choice)
    USERNAME_FIELD = 'D_username','D_email'

class PatientRegstration(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=200)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    Gender_choices = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    patient_choices = Gender_choices = [(1, 'Diagonistics'), (2, 'Followup'), (3, 'Prevention'), (4, 'Emergency')]
    gender = models.IntegerField(choices=Gender_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    patient_type = models.IntegerField(choices=patient_choices)
    age = models.IntegerField()
    queue_choices = [(0, 'YES'), (1, 'NO')]
    isinqueue =  models.IntegerField(choices=queue_choices)
    predictedtime  =  models.IntegerField()
    actualtime = models.IntegerField()
    DoctorInfo = models.ForeignKey(DoctorInfo,on_delete = models.CASCADE,null=True) 
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


    

