# Generated by Django 4.2.4 on 2024-09-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignalThree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
            ],
        ),
    ]
