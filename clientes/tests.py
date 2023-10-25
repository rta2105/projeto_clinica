from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.db.models import Count
from django.db.models import Sum
from .models import Medico, Agenda, Especialidade, Unidade, Consulta, Horario, AgendaManager, AgendaManager

class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("accounts:index")
    
class MedicoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    """
    class para visualizar o formulario do médico
    """
    model = Medico
    fields = ['nome', 'crm', 'especialidade', 'unidade']
    template_name = 'medicos/cadastro.html'
    success_url = reverse_lazy('medicos:medico_lista')

class MedicoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    model = Medico
    template_name = 'medicos/medicos_list.html'
    paginate_by = 10

class EspecialidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Especialidade
    fields = ['nome']
    template_name = 'medicos/especialidade_list.html'
    success_url = reverse_lazy('medicos:especialidade_lista')

class EspecialidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    model = Especialidade
    template_name = 'medicos/especialidade_list.html'
    paginate_by = 10

class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Agenda
    fields = ['medico', 'dia', 'horario_inicio', 'horario_fim']
    template_name = 'medicos/agenda_cadastro.html'
    success_url = reverse_lazy('medicos:agenda_lista')

class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    model = Agenda
    template_name = 'medicos/agenda_list.html'
    paginate_by = 10

class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    template_name = 'medicos/agenda_confirm_delete.html'
    success_url = reverse_lazy('medicos:agenda_lista')

class EspecialidadeUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Especialidade
    fields = ['nome']
    template_name = 'medicos/especialidade_form.html'
    success_url = reverse_lazy('medicos:especialidade_lista')

class UnidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Unidade
    fields = ['nome']
    template_name = 'medicos/unidade_form.html'
    success_url = reverse_lazy('medicos:unidade_lista')

class UnidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    model = Unidade
    template_name = 'medicos/unidade_list.html'
    paginate_by = 10

class UnidadeUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Unidade
    fields = ['nome']
    template_name = 'medicos/unidade_form.html'
    success_url = reverse_lazy('medicos:unidade_lista')

class MedicoUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Medico
    fields = ['nome', 'crm', 'especialidade', 'unidade']
    template_name = 'medicos/medico_form.html'
    success_url = reverse_lazy('medicos:medico_lista')

class MedicoDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Medico
    template_name = 'medicos/medico_confirm_delete.html'
    success_url = reverse_lazy('medicos:medico_lista')

class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Agenda
    fields = ['medico', 'dia', 'horario_inicio', 'horario_fim']
    template_name = 'medicos/agenda_form.html'
    success_url = reverse_lazy('medicos:agenda_lista')

class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    template_name = 'medicos/agenda_confirm_delete.html'
    success_url = reverse_lazy('medicos:agenda_lista')
