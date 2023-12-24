from django import forms
from .models import TaskCatagory

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = TaskCatagory
        fields = '__all__'