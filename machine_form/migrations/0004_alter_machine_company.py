# Generated by Django 5.1.1 on 2024-12-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_form', '0003_machine_complaints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='company',
            field=models.CharField(default='', max_length=255),
        ),
    ]