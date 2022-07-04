# Generated by Django 4.0.5 on 2022-06-24 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Naissance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_registre', models.CharField(max_length=150, verbose_name='Numero du Registre')),
                ('annee', models.IntegerField(verbose_name='Annee de Naissance')),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=150, verbose_name='Precise le sexe')),
                ('nom', models.CharField(max_length=250, verbose_name='Nom')),
                ('prenoms', models.CharField(max_length=250, verbose_name='Prenoms')),
                ('date_naiss', models.DateField(verbose_name='Date de Naissance')),
                ('heure_naiss', models.TimeField(verbose_name='Heure de Naissance')),
                ('pere', models.CharField(blank=True, max_length=250, verbose_name='Nom et Prénoms du Pere')),
                ('profession_pere', models.CharField(blank=True, max_length=250, verbose_name='Profession du Pere')),
                ('mere', models.CharField(max_length=250, verbose_name='Nom et Prénoms de la Mere')),
                ('profession_mere', models.CharField(max_length=250, verbose_name='Profession de la Mere')),
                ('ajouter_le', models.DateTimeField(auto_now_add=True)),
                ('modifier_le', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Acte de naissance',
                'verbose_name_plural': 'Actes de Naissance',
            },
        ),
    ]
