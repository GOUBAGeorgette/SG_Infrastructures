# Generated by Django 5.1.1 on 2024-10-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra_track', '0002_remove_panne_infrastructure_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='panne',
            name='status',
            field=models.CharField(choices=[('en_attente', 'En attente'), ('resolue', 'Résolue'), ('en_cours', 'En cours')], default='en_attente', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='panne',
            name='titre',
            field=models.CharField(max_length=100),
        ),
    ]
