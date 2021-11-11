from django  import forms

from django import forms
from django.db.models import fields
from .models import Lessonscore



class Lessonform(forms.ModelForm):
    class Meta :
        model = Lessonscore
        fields = '__all__'
