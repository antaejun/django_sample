from django import forms

from backend.models import TblHelpdesk

class HelpdeskForm(forms.ModelForm):
    
    class Meta:
        model = TblHelpdesk
        fields = ['type','sub_type','title','content','user_id']