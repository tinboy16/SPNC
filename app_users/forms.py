from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email này đã được sử dụng ở tài khoản khác.")
        return email

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = 'teacher'
    student = 'student'
    user_types = [
        (student, 'student'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')
