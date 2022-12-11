import datetime

from django.forms import ModelForm
from django import forms
from profileaccount.models import Profile
from django.forms.widgets import SelectDateWidget



class ProfileForm(ModelForm):
    # birthday = forms.DateField(label='Дата рождения', initial=datetime.date.today(),
    #                            input_formats=('%D-%M-%Y'),
    #                            widget=SelectDateWidget(years=range(1950, datetime.date.today().year+50)))
    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'avatar', 'birthday','email')




