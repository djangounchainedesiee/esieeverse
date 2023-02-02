# Generated by Django 4.1.3 on 2023-02-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0006_remove_publication_contient_multimedia_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='choix',
            constraint=models.UniqueConstraint(fields=('id', 'evenement', 'utilisateur'), name='unique_vote_user'),
        ),
    ]
