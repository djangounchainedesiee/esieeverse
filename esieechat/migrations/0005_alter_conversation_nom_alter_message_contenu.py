# Generated by Django 4.1.3 on 2022-11-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esieechat', '0004_rename_id_conversation_convutilisateur_conversation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='nom',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='contenu',
            field=models.CharField(max_length=125),
        ),
    ]
