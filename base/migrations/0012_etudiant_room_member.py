# Generated by Django 3.2.16 on 2023-03-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_detection_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='room_member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.roommember'),
        ),
    ]
