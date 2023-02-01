# Generated by Django 4.1.3 on 2023-02-01 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esieeverse', '0005_remove_promotion_annee_debut'),
        ('publication', '0004_alter_evenement_date_debut'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='utilisateur',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='esieeverse.utilisateur'),
            preserve_default=False,
        ),
    ]
