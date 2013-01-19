from django import forms

class DefaultForm(forms.Form):
    label_name = forms.CharField(max_length=100,
                                 help_text="Example block-level help text here.",
                                 widget=forms.TextInput(attrs={'placeholder': 'Type something...'}))
    check_me_out = forms.BooleanField(required=False)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'input-medium search-query'}))

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False)

