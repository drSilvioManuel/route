# Generated by Django 2.2.1 on 2019-05-05 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_street', to='nav.Street')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_street', to='nav.Street')),
            ],
            options={
                'unique_together': {('start', 'destination')},
            },
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_index', models.BigIntegerField(default=None)),
                ('path_text', models.TextField(default=None)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.Route')),
            ],
            options={
                'unique_together': {('route', 'path_index')},
            },
        ),
    ]
