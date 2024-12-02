from django.core.management.base import BaseCommand
from members.models import ProgramType, SubGroup

class Command(BaseCommand):
    help = 'Load initial data for programs and subgroups'

    def handle(self, *args, **kwargs):
        # Create instrumental programs
        instrumental_programs = [
            "Programa académico Orquestal",
            "Programa académico de Iniciación Musical",
            "Programa académico Simón Bolívar",
            "Programa académico Alma Llanera",
            "Programa académico de Música Popular y otros géneros"
        ]
        
        for program_name in instrumental_programs:
            ProgramType.objects.get_or_create(
                name=program_name,
                is_instrumental=True
            )

        # Create coral program and subgroups
        coral_program, _ = ProgramType.objects.get_or_create(
            name="Programa académico Coral",
            is_instrumental=False
        )

        coral_subgroups = [
            "Coral Filarmónica Federico Núñez Corona",
            "Coro Sinfónico Juvenil"
        ]

        for subgroup_name in coral_subgroups:
            SubGroup.objects.get_or_create(
                name=subgroup_name,
                program=coral_program
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))