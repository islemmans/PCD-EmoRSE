# Generated by Django 3.2.16 on 2023-04-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_remove_etudiant_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='etudiant',
            field=models.CharField(max_length=100),
        ),
    ]
