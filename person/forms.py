from django.forms import ModelForm
from .models import PersonModel


class PersonForm(ModelForm):
    class Meta:
        model = PersonModel
        fields = '__all__'
