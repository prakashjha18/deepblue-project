from django.contrib import admin

# from .forms import PatientRegstrationForm
# Register your models here.

from .models import PatientRegstration
from .models import DoctorInfo

admin.site.register(PatientRegstration)
admin.site.register(DoctorInfo)

