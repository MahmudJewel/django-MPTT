from django import forms
from second.models import Descriptions,Tag
# from mptt.forms import ModelChoiceField

class Descriptions_Form(forms.ModelForm):
    # tag= forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Descriptions
        fields = ["tag", "title", "desc"]
        widgets = {
            'tag': forms.CheckboxSelectMultiple, # many-to-many field will show as checkbox
            # 'tag' : ModelChoiceField(queryset=Tag.objects.all())
        }
