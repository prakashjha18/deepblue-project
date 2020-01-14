# Generated by Django 2.2.7 on 2020-01-14 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRegstration',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=200)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient_type', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=10)),
            ],
        ),
    ]
