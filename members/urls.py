from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberRegistrationView.as_view(), name='member_registration'),
    path('ajax/load-subgroups/', views.load_subgroups, name='ajax_load_subgroups'),
    path('success/', views.registration_success, name='registration_success'),
]