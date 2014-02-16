from django import forms
from TheDive.models import Dumpster, Food, FoodGroup

class FoodGroupForm(forms.ModelForm):
    foodgroup_choices=  (
                        (Produce, 'Produce'),
                        (Dairy,'Dairy'),
                        (Meat, 'Meat'),
                        (Bread, 'Bread'),
    )
    foodgroup=forms.ChoiceField()