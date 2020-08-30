from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label='Kullanici Adi')
    password = forms.CharField(label='Parola',widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length= 50, label = 'Kullanici Adi')
    password = forms.CharField(max_length= 20, label = 'Parola', widget=forms.PasswordInput)
    confrim  = forms.CharField(max_length=20, label = 'Paralayi Dogrula', widget= forms.PasswordInput)
    

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confrim  = self.cleaned_data.get('confrim')

        if password and confrim and password != confrim:
            raise forms.ValidationError('Parolalar Eslesmiyor')
        
        values = {
            'username' : username,
            'password' : password,
        }
        return values