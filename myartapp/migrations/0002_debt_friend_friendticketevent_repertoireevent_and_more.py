# Generated by Django 4.2.10 on 2024-03-11 18:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myartapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('full_name', models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='FriendTicketEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myartapp.friend', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepertoireEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
                ('description', models.TextField(blank=True)),
                ('duration', models.DurationField(blank=True)),
                ('age_limit', models.IntegerField(blank=True)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('director', models.CharField(blank=True, max_length=200)),
                ('cast', models.JSONField(blank=True, default=list)),
                ('event_url', models.URLField(blank=True)),
                ('images_url', models.JSONField(blank=True, default=list)),
                ('want_to_go', models.BooleanField(default=False)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(unique=True)),
                ('tickets_url', models.URLField(blank=True)),
                ('repertoire_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myartapp.repertoireevent', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(unique=True)),
                ('repertoire_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myartapp.repertoireevent', unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='culturalcenter',
            name='image',
        ),
        migrations.AddField(
            model_name='culturalcenter',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='culturalcenter',
            name='poster_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='culturalcenter',
            name='repertoire_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='culturalcenter',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='culturalcenter',
            name='name',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='culturalcenter',
            name='poster',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='repertoireevent',
            name='cultural_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myartapp.culturalcenter', unique=True),
        ),
        migrations.AddField(
            model_name='friendticketevent',
            name='ticket_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myartapp.ticketevent', unique=True),
        ),
        migrations.AddField(
            model_name='debt',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myartapp.friend', unique=True),
        ),
    ]