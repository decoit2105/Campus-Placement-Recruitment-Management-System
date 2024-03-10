from django.contrib import admin

# Register your models here.
from .models import Aspirant,Employer,Jobprofile,Job,Applyjob


admin.site.register(Aspirant)
admin.site.register(Employer)
admin.site.register(Jobprofile)
admin.site.register(Job)
admin.site.register(Applyjob)