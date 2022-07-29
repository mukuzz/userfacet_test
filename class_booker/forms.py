from django import forms
import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

weekday_re = re.compile(r"(Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day")
time_re = re.compile(r"")

def validate_capitalized(value):
    if value != value.capitalize():
        raise ValidationError('Invalid (not capitalized) value: %(value)s',
                              code='invalid',
                              params={'value': value})


class BookingRequest(forms.Form):
    full_name = forms.CharField(max_length=256)
    email_address = forms.EmailField(max_length=256)
    weekday = forms.CharField(validators=[validate_capitalized, RegexValidator(regex=weekday_re)])
    start_time = forms.CharField(max_length=10)
    end_time = forms.CharField(max_length=10)
