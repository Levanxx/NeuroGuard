# Generated by Django 5.2 on 2025-05-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('ataque', 'Ataque'), ('anomalia', 'Anomalía')], max_length=10)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('dispositivo', models.CharField(max_length=100)),
            ],
        ),
    ]
