# Generated by Django 2.0 on 2018-02-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coolness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField()),
                ('name', models.CharField(max_length=42)),
            ],
            options={
                'verbose_name': 'test',
                'ordering': ['identifier'],
            },
        ),
    ]
