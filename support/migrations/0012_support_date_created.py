# Generated by Django 4.0.6 on 2022-07-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0011_alter_support_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
    ]