# Generated by Django 3.1 on 2020-08-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_x', models.IntegerField()),
                ('point_y', models.IntegerField()),
            ],
        ),
    ]
