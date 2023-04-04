# Generated by Django 4.1.3 on 2023-03-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('esieeverse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=125)),
                ('contenu', models.TextField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esieeverse.utilisateur')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes_utilisateur', to='esieeverse.utilisateur')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes_utilisateur', to='esieeverse.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=125)),
                ('contenu', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteur', to='esieeverse.utilisateur')),
                ('utilisateur_inscrits', models.ManyToManyField(blank=True, related_name='utilisateur_inscrits', to='esieeverse.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Choix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.evenement')),
                ('utilisateurs', models.ManyToManyField(blank=True, to='esieeverse.utilisateur')),
            ],
        ),
    ]
