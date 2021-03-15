# Generated by Django 3.1.7 on 2021-03-14 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20210313_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pokemon_entities.pokemon'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='pokemon_entities.pokemon'),
        ),
    ]
