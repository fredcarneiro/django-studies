# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('applicant', models.ForeignKey(to='profiles.Profile', related_name='made_invitations')),
                ('invited', models.ForeignKey(to='profiles.Profile', related_name='received_invitations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
