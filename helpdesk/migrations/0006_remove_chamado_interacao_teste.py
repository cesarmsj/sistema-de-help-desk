# Generated by Django 3.2.4 on 2021-06-24 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20210624_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamado_interacao',
            name='teste',
        ),
    ]
