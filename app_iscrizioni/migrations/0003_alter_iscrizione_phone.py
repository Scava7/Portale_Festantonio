# Generated by Django 5.2.3 on 2025-06-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_iscrizioni', '0002_alter_iscrizione_options_iscrizione_comune_residenza_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iscrizione',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
