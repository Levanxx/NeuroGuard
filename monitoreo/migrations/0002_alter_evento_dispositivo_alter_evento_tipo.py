# Generated by Django 5.2 on 2025-05-03 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='dispositivo',
            field=models.CharField(blank=True, choices=[('almohada', 'Almohada Inteligente'), ('anillo', 'Anillo Inteligente'), ('watch', 'Smartwatch')], max_length=50),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('ataque', 'Ataque'), ('anomalia', 'Anomalía')], max_length=20),
        ),
    ]
