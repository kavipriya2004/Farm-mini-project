    # forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Farmer,Farm,Crop,Livestock,Expense
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FarmerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        exclude = ['user']  # Exclude the 'user' field as it will be populated automatically

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name', 'location', 'total_acres', 'description']

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = [ 'crop_name', 'planting_date', 'harvesting_date', 'yield_amount', 'notes']



class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = [ 'livestock_type', 'quantity', 'health_status', 'notes']

    def __init__(self, *args, **kwargs):
        super(LivestockForm, self).__init__(*args, **kwargs)
        # You can customize the form fields here if needed

class ExpenseForm(forms.ModelForm):
    farm_name = forms.CharField(max_length=255)
    class Meta:
        model = Expense
        fields = ['farm','expense_type','expense_date', 'amount', 'description']

    def clean_farm_name(self):
        farm_name = self.cleaned_data.get('farm_name')
        # Check if the farm exists
        try:
            farm = Farm.objects.get(farm_name=farm_name)
        except Farm.DoesNotExist:
            raise ValidationError('Farm does not exist.')
        return farm_name

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['budget']