# Generated by Django 2.2.7 on 2020-01-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientregstration',
            name='actualtime',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientregstration',
            name='isinqueue',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientregstration',
            name='predictedtime',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientregstration',
            name='age',
            field=models.IntegerField(),
        ),
    ]
