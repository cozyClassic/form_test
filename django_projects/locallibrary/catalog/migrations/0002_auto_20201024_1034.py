# Generated by Django 3.1.2 on 2020-10-24 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mymodelname',
            options={'ordering': ['-my_field_name'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]