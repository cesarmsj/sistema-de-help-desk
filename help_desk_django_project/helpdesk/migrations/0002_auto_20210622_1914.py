# Generated by Django 3.2.4 on 2021-06-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='123456', max_length=20)),
                ('nome', models.CharField(max_length=50)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('cidade', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]