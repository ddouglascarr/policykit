# Generated by Django 3.2.2 on 2021-09-02 15:10

from django.db import migrations, models
import django.db.models.deletion
import policyengine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discord', '0001_initial'),
        ('policyengine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordCommunity',
            fields=[
                ('communityplatform_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.communityplatform')),
                ('team_id', models.CharField(max_length=150, unique=True, verbose_name='team_id')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('policyengine.communityplatform',),
        ),
        migrations.CreateModel(
            name='DiscordCreateChannel',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('channel_id', models.BigIntegerField(blank=True)),
                ('name', models.TextField()),
            ],
            options={
                'permissions': (('can_execute_discordcreatechannel', 'Can execute discord create channel'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='DiscordDeleteChannel',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('channel_id', models.BigIntegerField()),
            ],
            options={
                'permissions': (('can_execute_discorddeletechannel', 'Can execute discord delete channel'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='DiscordDeleteMessage',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('channel_id', models.BigIntegerField()),
                ('message_id', models.BigIntegerField()),
                ('text', models.TextField(blank=True, default='')),
            ],
            options={
                'permissions': (('can_execute_discorddeletemessage', 'Can execute discord delete message'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='DiscordPostMessage',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('channel_id', models.BigIntegerField()),
                ('message_id', models.BigIntegerField()),
                ('text', models.TextField()),
            ],
            options={
                'permissions': (('can_execute_discordpostmessage', 'Can execute discord post message'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='DiscordRenameChannel',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('channel_id', models.BigIntegerField()),
                ('name', models.TextField()),
                ('name_old', models.TextField(blank=True, default='')),
            ],
            options={
                'permissions': (('can_execute_discordrenamechannel', 'Can execute discord rename channel'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('communityuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.communityuser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('policyengine.communityuser',),
            managers=[
                ('objects', policyengine.models.PolymorphicUserManager()),
            ],
        ),
    ]
