# Generated by Django 3.1 on 2020-08-30 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_groops'),
    ]

    operations = [
        migrations.AddField(
            model_name='groops',
            name='about',
            field=models.TextField(default="It's text about groop"),
            preserve_default=False,
        ),
    ]
