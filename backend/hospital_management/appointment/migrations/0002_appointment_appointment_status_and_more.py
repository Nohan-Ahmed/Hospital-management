# Generated by Django 5.0.7 on 2024-08-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(choices=[('Pendding', 'Pendding'), ('Runing', 'Runing'), ('Complated', 'Complated')], default='Pendding', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=50),
        ),
    ]
