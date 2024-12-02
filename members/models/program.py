from django.db import models

class ProgramType(models.Model):
    name = models.CharField(max_length=100)
    is_instrumental = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"