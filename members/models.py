from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ProgramType(models.Model):
    name = models.CharField(max_length=100)
    is_instrumental = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class SubGroup(models.Model):
    program = models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    VOICE_CHOICES = [
        ('soprano', 'Soprano'),
        ('contralto', 'Contralto'),
        ('tenor', 'Tenor'),
        ('bajo', 'Bajo'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField()
    age = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(100)])
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    program = models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    subgroup = models.ForeignKey(SubGroup, on_delete=models.SET_NULL, null=True, blank=True)
    instrument = models.CharField(max_length=100, blank=True, null=True)
    voice_type = models.CharField(max_length=20, choices=VOICE_CHOICES, blank=True, null=True)
    has_scholarship = models.BooleanField(default=False)
    medical_conditions = models.TextField(blank=True)
    
    # Fields for minor's legal representative
    is_minor = models.BooleanField(default=False)
    representative_name = models.CharField(max_length=200, blank=True, null=True)
    representative_id = models.CharField(max_length=20, blank=True, null=True)
    representative_contact = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"