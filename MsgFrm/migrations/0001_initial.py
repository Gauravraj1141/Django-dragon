# Generated by Django 4.0.5 on 2022-12-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=44)),
                ('email', models.EmailField(max_length=44)),
                ('phone', models.CharField(max_length=44)),
            ],
        ),
    ]