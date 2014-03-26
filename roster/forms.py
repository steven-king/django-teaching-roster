# roster/forms.py

from django import forms
from roster import models as m
 
class addCourseForm(forms.Form):
    name = forms.CharField(max_length=256)
    callnumber = forms.CharField(max_length=4)
    
    


class addCourseModelForm(forms.ModelForm):
    class Meta:
        model = m.Course