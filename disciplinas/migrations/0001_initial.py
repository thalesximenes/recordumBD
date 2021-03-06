# Generated by Django 4.0.6 on 2022-07-04 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tema', models.CharField(max_length=100)),
                ('aula', models.FileField(blank=True, upload_to='aulas')),
                ('mapa', models.ImageField(upload_to='mapa_Aula')),
            ],
        ),
        migrations.CreateModel(
            name='EixosTematico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MapasTexto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UltimaSessao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disciplinas.aulas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_Disciplinas')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disciplinas.eixostematico')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disciplinas.aulas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='aulas',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disciplinas.disciplinas'),
        ),
        migrations.AddField(
            model_name='aulas',
            name='mapasTexto',
            field=models.ManyToManyField(to='disciplinas.mapastexto'),
        ),
    ]
