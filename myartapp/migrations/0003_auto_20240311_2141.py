# Generated by Django 4.2.10 on 2024-03-11 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myartapp', '0002_debt_friend_friendticketevent_repertoireevent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='culturalcenter',
            name='poster',
        ),
    ]