# Generated by Django 3.1 on 2020-08-30 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20200823_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
            ],
        ),
    ]
