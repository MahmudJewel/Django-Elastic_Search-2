# Generated by Django 3.2 on 2022-11-09 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Comments',
        ),
    ]