# Generated by Django 3.0.7 on 2020-07-01 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200617_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoetype',
            name='style',
            field=models.CharField(max_length=20),
        ),
    ]
