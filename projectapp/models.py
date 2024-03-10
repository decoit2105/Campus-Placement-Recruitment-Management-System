from django.db import models

class Aspirant(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=50,blank=False)
    dob=models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    aspuname = models.CharField(max_length=50, blank=False, unique=True)
    pwd = models.CharField(max_length=50, blank=False)
    cpwd = models.CharField(max_length=50, blank=False)
    dept = models.CharField(max_length=100, blank=False)
    phno = models.BigIntegerField(blank=False,unique=True)

    def __str__(self):
        return self.aspuname
    

    class Meta:
        db_table = "aspirant_table"


class Employer(models.Model):
    fullname=models.CharField(max_length=50,blank=False)
    dob=models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    empuname = models.CharField(max_length=50, blank=False, unique=True)
    pwd = models.CharField(max_length=50, blank=False)
    cpwd = models.CharField(max_length=50, blank=False)
    dept = models.CharField(max_length=100, blank=False)
    phno = models.BigIntegerField(blank=False,unique=True)

    class Meta:
        db_table = "emp_table"


class Jobprofile(models.Model):
    aspuname = models.CharField(max_length=50,unique=True,blank=False)
    sscresult = models.IntegerField(blank=False,default=0)
    interresult = models.IntegerField(blank=False,default=0)
    backlogs = models.IntegerField(blank=False,default=0)
    btechresult = models.IntegerField(blank=False,default=0)
    skills = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = "jobprofile_table"


class Job(models.Model):
    jid = models.AutoField(primary_key = True)
    empuname = models.CharField(max_length=50,blank=False)
    jrole=models.CharField(max_length=50,unique=True,blank=False)
    jdesc = models.CharField(max_length=200,blank=False)
    mode_choices = (("On Campus", "On Campus"), ("Off Campus", "Off Campus"))
    mode = models.CharField(blank=False, choices=mode_choices, max_length=10)
    fromdate = models.DateField(blank=False,default=None)
    todate = models.DateField(blank=False,default=None)
    min_ssc = models.IntegerField(blank=False,default=0)
    min_inter = models.IntegerField(blank=False,default=0)
    max_backlogs = models.IntegerField(blank=False,default=0)
    min_btech = models.IntegerField(blank=False,default=0)

    def __str__(self):
        return str(self.jid)

    class Meta:
        db_table = "job_table"


class Applyjob(models.Model):
    aid = models.AutoField(primary_key=True)
    aspuname = models.CharField(max_length=50,blank = False)
    jid = models.PositiveIntegerField(blank= False)
    appliedtime = models.DateTimeField(blank=False,auto_now=True)
    status = models.CharField(max_length=50, blank=False,default="Applied")

    class Meta:
        db_table = "applyjob_table"
#apply jobs model{id, aspirant uname, jid, time, status}
#more fields in jobs and jobprofiled{ssc result, inter result, backlogs allowed, btech, company name}