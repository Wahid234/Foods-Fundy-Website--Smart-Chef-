from django import forms
from .models import UserMealIngredient
class UserMealIngredientForm(forms.ModelForm):

       class Meta:
        model = UserMealIngredient
        fields = '__all__'