# -*- coding: utf-8 -*-
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

CHOICES = (
        ('option1', "Option one is this and that—be sure to include why it's great"),
        ('option2', "Option two can be something else and selecting it will deselect option one"),
        )
class CheckboxRadioForm(forms.Form):
    opt1 = forms.BooleanField(label="Option one is this and that—be sure to include why it's great")
    radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class InlineCheckboxesForm(forms.Form):
    opt1 = forms.BooleanField(label="1")
    opt2 = forms.BooleanField(label="2")
    opt3 = forms.BooleanField(label="3")

SELECT_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        )

class SelectForm(forms.Form):
    select1 = forms.ChoiceField(choices=SELECT_CHOICES, label="")
    select2 = forms.ChoiceField(widget=forms.SelectMultiple, choices=SELECT_CHOICES, label="")
