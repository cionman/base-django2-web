from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import User, Profile


class SignupForm(UserCreationForm):
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = '이메일을 입력해주세요.'
        self.fields['username'].label = '이메일'

        self.fields['phone'].help_text = '전화번호를 입력해주세요.'
        self.fields['phone'].label = '전화번호'

        self.fields['address'].help_text = '주소를 입력해주세요.'
        self.fields['address'].label = '주소'

    def save(self):
        user = super().save(commit=False)
        user.email = user.username
        user.save()

        phone = self.cleaned_data.get('phone', None)
        address = self.cleaned_data.get('address', None)

        Profile.objects.create(user=user, phone=phone, address=address)

        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('phone', 'address')

    '''
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)
        return value
    '''


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']
