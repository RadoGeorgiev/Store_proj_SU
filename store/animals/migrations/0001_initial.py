# Generated by Django 2.2.4 on 2019-08-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('breed', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('kind', models.CharField(choices=[('D', 'Dog'), ('C', 'Cat')], max_length=1)),
                ('owner', models.ForeignKey(default=0, on_delete=None, to='animals.Owner')),
            ],
        ),
    ]
