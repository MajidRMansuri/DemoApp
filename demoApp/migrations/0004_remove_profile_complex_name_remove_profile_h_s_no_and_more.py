# Generated by Django 4.0.5 on 2022-06-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0003_alter_profile_shop_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Complex_Name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='H_S_no',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Nr_Landmark',
        ),
    ]
