# Generated by Django 4.2.6 on 2023-10-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_cidade_capital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]