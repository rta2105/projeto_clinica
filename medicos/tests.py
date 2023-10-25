from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .models import Medico, Agenda, Especialidade, Unidade, Consulta, Horario



class TestMedico(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='teste',
            password='teste'
        )   
        self.user.save()
        self.client.login(username='teste', password='teste')
        self.medico = Medico.objects.create(
            nome='teste',
            crm='123456',
            especialidade=Especialidade.objects.create(nome='teste'),
            unidade=Unidade.objects.create(nome='teste')
        )   
        self.medico.save()
        self.agenda = Agenda.objects.create(
            medico=self.medico,
            dia='2021-01-01',
            horario_inicio='08:00',
            horario_fim='09:00'
        )
        self.agenda.save()
        self.consulta = Consulta.objects.create(
            agenda=self.agenda,
            paciente=self.user
        )
        self.consulta.save()
        self.horario = Horario.objects.create(
            horario_inicio='08:00',
            horario_fim='09:00'
        )
        self.horario.save()
        self.especialidade = Especialidade.objects.create(
            nome='teste'
        )
        self.especialidade.save()
        self.unidade = Unidade.objects.create(
            nome='teste'
        )
        self.unidade.save()
        self.user = get_user_model().objects.create_user(
            username='teste',
            password='teste'
        )

    def test_medico_cadastro(self):
        response = self.client.get(reverse('medicos:medico_cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/cadastro.html')
        self.assertContains(response, 'Cadastro de Médico')
        self.assertContains(response, 'Nome')
        self.assertContains(response, 'CRM')
        self.assertContains(response, 'Especialidade')
        self.assertContains(response, 'Unidade')
        self.assertContains(response, 'Salvar')
        self.assertContains(response, 'Voltar')
        self.assertContains(response, 'teste')
        self.assertContains(response, '123456')
        self.assertContains(response, 'teste')
        self.assertContains(response, 'teste')
    
    def test_medico_lista(self):
        response = self.client.get(reverse('medicos:medicos_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/medicos_list.html')
        self.assertContains(response, 'Lista de Médicos')
        self.assertContains(response, 'teste')
        self.assertContains(response, '123456')
        self.assertContains(response, 'teste')
        self.assertContains(response, 'teste')
        self.assertContains(response, 'Editar')
        self.assertContains(response, 'Excluir')
        self.assertContains(response, 'Voltar')
        
    def test_especialidade_cadastro(self):
        response = self.client.get(reverse('medicos:especialidade_cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/especialidade_form.html')
        self.assertContains(response, 'Cadastro de Especialidade')
        self.assertContains(response, 'Nome')
        self.assertContains(response, 'Salvar')
        self.assertContains(response, 'Voltar')
        self.assertContains(response, 'teste')
    
    def test_especialidade_lista(self):
        response = self.client.get(reverse('medicos:especialidade_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/especialidade_list.html')
        self.assertContains(response, 'Lista de Especialidades')
        self.assertContains(response, 'teste')
        self.assertContains(response, 'Editar')
        self.assertContains(response, 'Excluir')
        self.assertContains(response, 'Voltar')
    
    def test_agenda_cadastro(self):
        response = self.client.get(reverse('medicos:agendar_consulta'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/agenda_form.html')
        self.assertContains(response, 'Agendar Consulta')
        self.assertContains(response, 'Médico')
        self.assertContains(response, 'Dia')
        self.assertContains(response, 'Horário de Início')
        self.assertContains(response, 'Horário de Fim')
        self.assertContains(response, 'Salvar')
        self.assertContains(response, 'Voltar')
        self.assertContains(response, 'teste')
        self.assertContains(response, '2021-01-01')
        self.assertContains(response, '08:00')
        self.assertContains(response, '09:00')
    
    def test_agenda_lista(self):
        response = self.client.get(reverse('medicos:agenda_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/agenda_list.html')
        self.assertContains(response, 'Lista de Agendas')
        self.assertContains(response, 'teste')
        self.assertContains(response, '2021-01-01')
        self.assertContains(response, '08:00')
        self.assertContains(response, '09:00')
        self.assertContains(response, 'Editar')
        self.assertContains(response, 'Excluir')
        self.assertContains(response, 'Voltar')
    
    def test_agenda_atualizar(self):
        response = self.client.get(reverse('medicos:agendar_consulta_atualizar', kwargs={'pk': self.agenda.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/agenda_form.html')
        self.assertContains(response, 'Agendar Consulta')
        self.assertContains(response, 'Médico')
        self.assertContains(response, 'Dia')
        self.assertContains(response, 'Horário de Início')
        self.assertContains(response, 'Horário de Fim')
        self.assertContains(response, 'Salvar')
        self.assertContains(response, 'Voltar')
        self.assertContains(response, 'teste')
        self.assertContains(response, '2021-01-01')
        self.assertContains(response, '08:00')
        self.assertContains(response, '09:00')
    
    def test_agenda_deletar(self):
        response = self.client.get(reverse('medicos:agendar_consulta_deletar', kwargs={'pk': self.agenda.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/agenda_confirm_delete.html')
        self.assertContains(response, 'Deletar Consulta')
        self.assertContains(response, 'Confirmar exclusão da consulta de teste')
        self.assertContains(response, 'Sim')
        self.assertContains(response, 'Não')
    
    def test_unidade_lista(self):
        response = self.client.get(reverse('medicos:unidade_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/unidade_list.html')
        self.assertContains(response, 'Lista de Unidades')
        self.assertContains(response, 'teste')
        self.assertContains(response, 'Editar')
        self.assertContains(response, 'Excluir')
        self.assertContains(response, 'Voltar')
    
    def test_unidade_cadastro(self):
        response = self.client.get(reverse('medicos:unidade_cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/unidade_form.html')
        self.assertContains(response, 'Cadastro de Unidade')
        self.assertContains(response, 'Nome')
        self.assertContains(response, 'Endereço')
        self.assertContains(response, 'Salvar')
        self.assertContains(response, 'Voltar')
        self.assertContains(response, 'teste')
        self.assertContains(response, 'teste')
    
    def test_login(self):
        response = self.client.get(reverse('medicos:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/login.html')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Usuário')
        self.assertContains(response, 'Senha')
        self.assertContains(response, 'Entrar')
        self.assertContains(response, 'Voltar')

    def test_logout(self):
        response = self.client.get(reverse('medicos:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('medicos:login'))
    
    def test_index(self):
        response = self.client.get(reverse('medicos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/index.html')
        self.assertContains(response, 'Bem vindo ao sistema de agendamento de consultas')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Cadastro')
        self.assertContains(response, 'Sistema de Agendamento de Consultas')
    
    def test_index_logado(self):
        self.client.login(username='teste', password='teste')
        response = self.client.get(reverse('medicos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/index.html')
        self.assertContains(response, 'Bem vindo ao sistema de agendamento de consultas')
        self.assertContains(response, 'Logout')
        self.assertContains(response, 'Cadastro')
        self.assertContains(response, 'Sistema de Agendamento de Consultas')

    def test_index_logado_admin(self):
        self.user.is_staff = True
        self.user.save()
        self.client.login(username='teste', password='teste')
        response = self.client.get(reverse('medicos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicos/index.html')
        self.assertContains(response, 'Bem vindo ao sistema de agendamento de consultas')
        self.assertContains(response, 'Logout')
        self.assertContains(response, 'Cadastro')
        self.assertContains(response, 'Sistema de Agendamento de Consultas')
        self.assertContains(response, 'Administrador')
    

