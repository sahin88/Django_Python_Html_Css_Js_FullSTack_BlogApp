# Generated by Django 3.2.1 on 2021-05-07 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalApp', '0006_alter_post_detail_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post_detail',
            new_name='post_detail_model',
        ),
    ]