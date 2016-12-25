from django import forms
from .models import CustomUser


class SignUpForm(forms.ModelForm) :
    class Meta:
        model


'''class SignUpForm(forms.ModelForm) :
    error_messages = {
        'password_mismatch': ("Password Mismatch"),
    }
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))
    class Meta :
        fields = ("email",)
        unique = {"email": True, 'username': True}
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "user_avatar", "user_details")
        widgets = {
            'user_details': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
'''
