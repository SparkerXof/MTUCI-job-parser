# Generated by Django 5.0.6 on 2024-07-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_auto_20240706_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationmodel',
            name='job',
            field=models.CharField(default='No', max_length=1000),
        ),
    ]