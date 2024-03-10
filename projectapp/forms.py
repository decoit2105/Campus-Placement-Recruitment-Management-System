from django import forms
from .models import Job,Jobprofile

class DateInput(forms.DateInput):
    input_type = "date"


"""class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Aspirant
        fields = "__all__"    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}    # additional features of the fields"""


class JobsForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = {"empuname"}
        labels = {"jrole" : "Job Role","jdesc":"Job Description","fromdate" : "Start Date","todate":"End Date","min_btech":"Minimum B.Tech Score(in Percentage)","min_ssc":"Minimum SSC Score(in Percentage)","min_inter":"Minimum Intermediate Score(in Percentage)","max_backlogs":"Maximum Number of Backlogs Allowed"}
        widgets = {"fromdate": DateInput(), "todate": DateInput()}


class JobprofileForm(forms.ModelForm):
    class Meta:
        model = Jobprofile
        fields = "__all__"
        exclude = {"aspuname"}
        labels = {"sscresult" : "Your SSC Result(in Percentage)","interresult":"Your Intermediate Score(in Percentage)","backlogs":"Number of Backlogs You currently have","btechresult":"Your B.Tech Result(in percentage)","skills":"Provide Your Skills"}