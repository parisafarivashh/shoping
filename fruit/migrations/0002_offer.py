# Generated by Django 3.0 on 2020-02-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=60)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
