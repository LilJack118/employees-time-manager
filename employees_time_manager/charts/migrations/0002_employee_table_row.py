# Generated by Django 3.2.8 on 2021-10-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='table_row',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
