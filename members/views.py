from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Member, SubGroup
from .forms import MemberRegistrationForm

class MemberRegistrationView(CreateView):
    model = Member
    form_class = MemberRegistrationForm
    template_name = 'members/registration.html'
    success_url = reverse_lazy('registration_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Miembros - El Sistema, núcleo Carabobo'
        return context

def load_subgroups(request):
    program_id = request.GET.get('program_id')
    subgroups = SubGroup.objects.filter(program_id=program_id)
    return JsonResponse([{'id': sg.id, 'name': sg.name} for sg in subgroups], safe=False)

def registration_success(request):
    return render(request, 'members/success.html')