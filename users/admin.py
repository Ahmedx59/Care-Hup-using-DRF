from django.contrib import admin
from users.models import User, PatientProfile, DoctorNurseProfile

admin.site.register(User)
admin.site.register(DoctorNurseProfile)
admin.site.register(PatientProfile)
