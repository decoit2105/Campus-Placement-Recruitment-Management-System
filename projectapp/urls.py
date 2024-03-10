from django.urls import path
from . import views
urlpatterns = [
    path("aspiranthome",views.aspiranthomefunction,name="aspiranthome"),
    path("employerhome",views.emphomefunction,name="employerhome"),
    path("aspprofile",views.aspprofilefunction,name="aspprofile"),
    path("empprofile",views.empprofilefunction,name="empprofile"),
    path("registration",views.registrationfunction,name="registration"),
    path("submitregister",views.registrationfunction,name="submitregister"),
    path("login",views.loginfunction,name="login"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("aboutaspirant/<str:aspuname>",views.aboutaspirant,name="aboutaspirant"),
    path("addjob",views.addjob,name="addjob"),
    path("applied/<int:jid>",views.applied,name = "applied"),
    path("viewjobs",views.viewjobs,name="viewjobs"),
    path("viewapplicants/<int:jid>",views.viewapplicants,name="viewapplicants"),
    path("asplogout",views.asplogout,name="asplogout"),
    path("emplogout",views.emplogout,name="emplogout"),
]