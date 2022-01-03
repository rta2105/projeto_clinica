# Generated by Django 4.0 on 2022-01-03 18:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('crm', models.CharField(max_length=200, verbose_name='CRM')),
                ('telefone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="O número precisa estar neste formato:                     '+99 99 9999-0000'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefone')),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='medicos.especialidade')),
            ],
        ),
    ]
