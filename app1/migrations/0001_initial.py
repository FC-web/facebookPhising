# Generated by Django 3.2.4 on 2021-06-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ui', models.CharField(max_length=18)),
                ('password', models.CharField(max_length=18)),
            ],
        ),
    ]