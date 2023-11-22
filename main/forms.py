from django import forms
from .models import LabTest, TestCategory, Doctor


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LabTestForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = LabTest
        fields = '__all__'


class DoctorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class TestCategoryForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = TestCategory
        fields = '__all__'