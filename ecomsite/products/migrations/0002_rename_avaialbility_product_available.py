# Generated by Django 5.1.7 on 2025-03-08 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avaialbility',
            new_name='available',
        ),
    ]
