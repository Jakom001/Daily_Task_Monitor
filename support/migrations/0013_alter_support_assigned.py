# Generated by Django 4.0.6 on 2022-07-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0012_support_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='assigned',
            field=models.CharField(max_length=255, verbose_name='Assigned To'),
        ),
    ]