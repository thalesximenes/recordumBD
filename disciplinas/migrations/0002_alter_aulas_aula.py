# Generated by Django 4.0.5 on 2022-06-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aulas',
            name='aula',
            field=models.FileField(blank=True, upload_to='aulas'),
        ),
    ]