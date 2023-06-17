from django import forms
from courses.models import CoursesImages


class MyModelForm(forms.ModelForm):
    class Meta:
        model = CoursesImages
        fields = ('image',)
