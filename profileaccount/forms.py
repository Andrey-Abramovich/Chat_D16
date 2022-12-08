from django.forms import ModelForm

from profileaccount.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'birthday', 'email')

