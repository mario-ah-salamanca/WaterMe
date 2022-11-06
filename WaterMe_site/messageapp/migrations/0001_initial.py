# Generated by Django 4.1.3 on 2022-11-06 03:48

from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('plantid', models.AutoField(primary_key=True, serialize=False)),
                ('plantName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TwilioAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssid', django_cryptography.fields.encrypt(models.CharField(max_length=80))),
                ('authToken', django_cryptography.fields.encrypt(models.CharField(max_length=80))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('sensorid', models.AutoField(primary_key=True, serialize=False)),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messageapp.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sender', models.CharField(max_length=250)),
                ('receiver', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=500)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messageapp.plant')),
            ],
        ),
    ]