# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contacts',
            field=models.ManyToManyField(related_name='_profile_contacts_+', to='profiles.Profile'),
        ),
    ]