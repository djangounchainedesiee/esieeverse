# Generated by Django 4.1.3 on 2023-03-06 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='auteur',
        ),
    ]
