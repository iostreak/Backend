# Generated by Django 5.1.6 on 2025-03-12 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=20)),
                ('Subject', models.CharField(max_length=20)),
                ('Message', models.CharField(max_length=200)),
            ],
        ),
    ]
