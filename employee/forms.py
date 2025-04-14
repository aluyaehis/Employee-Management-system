from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields_name, field in self.fields.items():
            field.widget.attrs.update({
                'style': 'width: 600px; padding:8px; margin-bottom: 10px;'
            })















        # fields = ['employee_id', 'employee_name', 'employee_email', 'employee_contact']
