from django.contrib import admin
from .models import ProgramType, SubGroup, Member

@admin.register(ProgramType)
class ProgramTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_instrumental')
    search_fields = ('name',)

@admin.register(SubGroup)
class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'program')
    list_filter = ('program',)
    search_fields = ('name',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_number', 'program', 'has_scholarship')
    list_filter = ('program', 'has_scholarship', 'is_minor')
    search_fields = ('first_name', 'last_name', 'id_number')
    fieldsets = (
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'id_number', 'birth_date', 'age', 'address')
        }),
        ('Contacto', {
            'fields': ('email', 'phone')
        }),
        ('Programa', {
            'fields': ('program', 'subgroup', 'instrument', 'voice_type', 'has_scholarship')
        }),
        ('Información Médica', {
            'fields': ('medical_conditions',)
        }),
        ('Representante Legal', {
            'fields': ('is_minor', 'representative_name', 'representative_id', 'representative_contact'),
            'classes': ('collapse',)
        })
    )