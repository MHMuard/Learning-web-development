from django import forms
from first_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        fields = ['name', 'roll', 'address', 'father_name']

        labels = {
            'name': 'Name of the Student',
            'roll': 'Student roll',
        }
        widgets = {
            'name': forms.TextInput(),
        }
        help_text = {
            'name': 'Write the full name of the Student'
        }
        error_messages = {
            'name': {'required': 'Your name is required'}
        }