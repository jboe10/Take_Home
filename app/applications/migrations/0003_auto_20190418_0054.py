# Generated by Django 2.2 on 2019-04-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20190418_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='Age',
            field=models.FloatField(),
        ),
    ]