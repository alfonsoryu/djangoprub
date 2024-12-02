from django import forms
from .models import Member, ProgramType, SubGroup

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'medical_conditions': forms.Textarea(attrs={'rows': 3}),
            'representative_contact': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subgroup'].queryset = SubGroup.objects.none()
        
        if 'program' in self.data:
            try:
                program_id = int(self.data.get('program'))
                self.fields['subgroup'].queryset = SubGroup.objects.filter(program_id=program_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subgroup'].queryset = self.instance.program.subgroup_set.all()

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        is_minor = age < 18 if age else False
        cleaned_data['is_minor'] = is_minor
        
        if is_minor:
            required_fields = ['representative_name', 'representative_id', 'representative_contact']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, 'Este campo es requerido para menores de edad.')
        
        program = cleaned_data.get('program')
        if program:
            if program.is_instrumental:
                if not cleaned_data.get('instrument'):
                    self.add_error('instrument', 'El instrumento es requerido para programas instrumentales.')
            else:
                if not cleaned_data.get('voice_type'):
                    self.add_error('voice_type', 'La tesitura vocal es requerida para programas corales.')
        
        return cleaned_data