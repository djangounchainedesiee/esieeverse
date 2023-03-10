# Generated by Django 4.1.3 on 2023-03-07 07:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_fin', models.PositiveSmallIntegerField(default=1900, validators=[django.core.validators.MinValueValidator(1900)])),
                ('filieres', models.ManyToManyField(to='esieeverse.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_de_profile', models.ImageField(null=True, upload_to='media/')),
                ('abonnements', models.ManyToManyField(blank=True, related_name='abonnements_utilisateur', to='esieeverse.utilisateur')),
                ('banis', models.ManyToManyField(blank=True, related_name='utilisateur_bannis', to='esieeverse.utilisateur')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esieeverse.classe')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esieeverse.filiere')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esieeverse.promotion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='classe',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esieeverse.filiere'),
        ),
    ]
