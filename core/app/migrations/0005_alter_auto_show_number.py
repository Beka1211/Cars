# Generated by Django 5.2.4 on 2025-07-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_auto_show_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto_show',
            name='number',
            field=models.CharField(max_length=8),
        ),
    ]
