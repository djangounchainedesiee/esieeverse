# Generated by Django 4.1.3 on 2022-12-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esieeverse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='annee_debut',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='annee_fin',
            field=models.DateField(auto_now_add=True),
        ),
    ]