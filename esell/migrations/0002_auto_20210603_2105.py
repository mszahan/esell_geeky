# Generated by Django 3.2.3 on 2021-06-03 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='use',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='ueer',
            new_name='user',
        ),
    ]