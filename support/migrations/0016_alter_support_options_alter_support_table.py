# Generated by Django 4.0.6 on 2022-07-14 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0015_alter_support_category_alter_support_solution'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='support',
            options={'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelTable(
            name='support',
            table='task',
        ),
    ]
