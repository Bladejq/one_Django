# Generated by Django 4.2.8 on 2024-01-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QalaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qala', models.CharField(max_length=100)),
                ('halyq', models.IntegerField()),
            ],
        ),
    ]