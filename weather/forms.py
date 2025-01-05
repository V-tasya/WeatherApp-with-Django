from .models import City
from django.forms import ModelForm, TextInput
# ModelForm is a django class which allows automatically create forms based on the model

class CityForm(ModelForm):
    #class meta is form which provides additional settings for form
    class Meta:
        # connected form with city model, form will mork with city's model fields
        model = City
        # defines which model fields will be used in the form
        fields = ['name']
        widgets = {'name' : TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Enter a city'
        })}