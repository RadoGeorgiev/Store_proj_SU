# Generated by Django 2.2.4 on 2019-08-15 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='owner',
        ),
    ]