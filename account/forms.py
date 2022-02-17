from django import forms
from .models import User


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
        self.fields['VIP_user'].disabled = True
        self.fields['is_author'].disabled = True
        self.fields['date_joined'].disabled = True

        self.fields['username'].help_text = None

    
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'first_name',
        'last_name',
        'VIP_user',
        'is_author',
        'date_joined',
    ]

