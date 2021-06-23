# Generated by Django 3.2.4 on 2021-06-22 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_auto_20210622_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('A', 'Aberto'), ('E', 'Em Andamento'), ('F', 'Finalizado')], max_length=1)),
                ('data_abertura', models.DateField()),
                ('data_fechamento', models.DateField(null=True)),
                ('fk_atendente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.atendente')),
                ('fk_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Chamado_Interacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('fk_chamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.chamado')),
            ],
        ),
    ]