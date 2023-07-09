from django import forms
from dashboard.models import UserFile


class UserFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']

class UploadFileForm(forms.Form):
    file = forms.FileField()