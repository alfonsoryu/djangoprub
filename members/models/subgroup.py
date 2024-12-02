from django.db import models

class SubGroup(models.Model):
    program = models.ForeignKey('members.ProgramType', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Subgrupo"
        verbose_name_plural = "Subgrupos"