from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey

class Especialidade(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    
    def __str__(self):
        return f'{self.nome}'

class Unidade(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    
    def __str__(self):
        return f'{self.nome}'

class AgendaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(dia__gte=date.today())

class Medico(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    email = models.EmailField(verbose_name="Email")
    crm = models.CharField(verbose_name="CRM", max_length=200)
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número precisa estar neste formato: \
                    '+99 99 9999-0000'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    especialidade = ForeignKey(Especialidade,
                               on_delete=models.CASCADE,
                               related_name='medicos')
    unidade = ForeignKey(Unidade, 
                         on_delete=models.CASCADE, 
                         related_name='medicos')
    
    def __str__(self):
        return f'{self.nome}'

def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Escolha um dia útil da semana.')

class Agenda(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agendas')
    dia = models.DateField(verbose_name="Dia", validators=[validar_dia])
    horario_inicio = models.TimeField(verbose_name="Horário de Início")
    horario_fim = models.TimeField(verbose_name="Horário de Fim")
    objects = AgendaManager()

    def __str__(self):
        return f'{self.medico} - {self.dia} - {self.horario_inicio} - {self.horario_fim}'
    
    class Meta:
        unique_together = ['medico', 'dia', 'horario_inicio', 'horario_fim']
        ordering = ['dia', 'horario_inicio']
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

class Consulta(models.Model):
    agenda = ForeignKey(Agenda, on_delete=models.CASCADE, related_name='consultas')
    paciente = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='consultas')
    data_agendamento = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.agenda} - {self.paciente} - {self.data_agendamento}'
    
    class Meta:
        unique_together = ['agenda', 'paciente']
        ordering = ['data_agendamento']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

class Horario(models.Model):
    horario_inicio = models.TimeField(verbose_name="Horário de Início")
    horario_fim = models.TimeField(verbose_name="Horário de Fim")
    
    def __str__(self):
        return f'{self.horario_inicio} - {self.horario_fim}'
    
    class Meta:
        ordering = ['horario_inicio']
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'

class HorarioAtendimento(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='horarios')
    dia = models.DateField(verbose_name="Dia", validators=[validar_dia])
    horario = ForeignKey(Horario, on_delete=models.CASCADE, related_name='horarios')
    
    def __str__(self):
        return f'{self.medico} - {self.dia} - {self.horario}'
    
    class Meta:
        unique_together = ['medico', 'dia', 'horario']
        ordering = ['dia', 'horario']
        verbose_name = 'Horário de Atendimento'
        verbose_name_plural = 'Horários de Atendimento'

class HorarioAtendimentoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(dia__gte=date.today())

class HorarioAtendimentoDisponivel(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='horarios_disponiveis')
    dia = models.DateField(verbose_name="Dia", validators=[validar_dia])
    horario = ForeignKey(Horario, on_delete=models.CASCADE, related_name='horarios_disponiveis')
    objects = HorarioAtendimentoManager()
    
    def __str__(self):
        return f'{self.medico} - {self.dia} - {self.horario}'
    
    class Meta:
        unique_together = ['medico', 'dia', 'horario']
        ordering = ['dia', 'horario']
        verbose_name = 'Horário de Atendimento Disponível'
        verbose_name_plural = 'Horários de Atendimento Disponíveis'

class HorarioAtendimentoDisponivelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(dia__gte=date.today())

class ConsultaDisponivel(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas_disponiveis')
    dia = models.DateField(verbose_name="Dia", validators=[validar_dia])
    horario_inicio = models.TimeField(verbose_name="Horário de Início")
    horario_fim = models.TimeField(verbose_name="Horário de Fim")
    objects = HorarioAtendimentoDisponivelManager()
    
    def __str__(self):
        return f'{self.medico} - {self.dia} - {self.horario_inicio} - {self.horario_fim}'
    
    class Meta:
        unique_together = ['medico', 'dia', 'horario_inicio', 'horario_fim']
        ordering = ['dia', 'horario_inicio']
        verbose_name = 'Consulta Disponível'
        verbose_name_plural = 'Consultas Disponíveis'