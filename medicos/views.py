from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class unidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):
    model = Unidade
    fields = ['nome', 'endereco']
    template_name = 'medicos/unidade_form.html'
    success_url = reverse_lazy('medicos:unidade_lista')

class unidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    model = Unidade
    template_name = 'medicos/unidade_list.html'
    paginate_by = 10



class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):
    model = Agenda
    fields = ['medico', 'dia', 'horario_inicio', 'horario_fim']
    template_name = 'medicos/agenda_form.html'
    success_url = reverse_lazy('medicos:agenda_lista')

medico_cadastro = MedicoCreateView.as_view()
medico_lista = MedicoListView.as_view()
especialidade_cadastro = EspecialidadeCreateView.as_view()
especialidade_lista = EspecialidadeListView.as_view()
agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()
especialidade_atualizar = EspecialidadeUpdateView.as_view()
unidade_cadastro = unidadeCreateView.as_view()
unidade_lista = unidadeListView.as_view()



