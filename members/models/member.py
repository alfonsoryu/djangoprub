from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Member(models.Model):
    VOICE_CHOICES = [
        ('soprano', 'Soprano'),
        ('contralto', 'Contralto'),
        ('tenor', 'Tenor'),
        ('bajo', 'Bajo'),
    ]

    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    id_number = models.CharField('Cédula', max_length=20, unique=True)
    birth_date = models.DateField('Fecha de nacimiento')
    age = models.IntegerField('Edad', validators=[MinValueValidator(5), MaxValueValidator(100)])
    address = models.TextField('Dirección')
    email = models.EmailField('Correo electrónico')
    phone = models.CharField('Teléfono', max_length=20)
    program = models.ForeignKey('members.ProgramType', verbose_name='Programa', on_delete=models.CASCADE)
    subgroup = models.ForeignKey('members.SubGroup', verbose_name='Subgrupo', on_delete=models.SET_NULL, null=True, blank=True)
    instrument = models.CharField('Instrumento', max_length=100, blank=True, null=True)
    voice_type = models.CharField('Tesitura Vocal', max_length=20, choices=VOICE_CHOICES, blank=True, null=True)
    has_scholarship = models.BooleanField('¿Recibe beca?', default=False)
    medical_conditions = models.TextField('Condiciones médicas', blank=True)
    
    is_minor = models.BooleanField('Es menor de edad', default=False)
    representative_name = models.CharField('Nombre del representante', max_length=200, blank=True, null=True)
    representative_id = models.CharField('Cédula del representante', max_length=20, blank=True, null=True)
    representative_contact = models.TextField('Contacto del representante', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"