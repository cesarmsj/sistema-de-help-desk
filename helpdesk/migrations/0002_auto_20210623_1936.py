# Generated by Django 3.2.4 on 2021-06-23 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendente',
            old_name='atendente',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cliente',
            new_name='user',
        ),
        migrations.AlterModelTable(
            name='atendente',
            table='helpdesk_atendente',
        ),
        migrations.AlterModelTable(
            name='cliente',
            table='helpdesk_cliente',
        ),
    ]
