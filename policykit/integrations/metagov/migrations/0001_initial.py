# Generated by Django 3.2.2 on 2021-09-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetagovConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': [('can_edit_metagov_config', 'Can edit Metagov config')],
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]
