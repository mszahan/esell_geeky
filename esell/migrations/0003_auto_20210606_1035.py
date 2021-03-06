# Generated by Django 3.2.3 on 2021-06-06 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esell', '0002_auto_20210603_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('delivary_mail', models.EmailField(max_length=254)),
                ('district', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=100)),
                ('postal', models.IntegerField()),
                ('division', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Rajshahi', 'Rajshahi'), ('Chittagong', 'Chittagong'), ('Khulna', 'Khulna'), ('Sylhet', 'Sylhet'), ('Mymenshingh', 'Mymenshingh'), ('Rangpur', 'Rangpur')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esell.customer'),
        ),
        migrations.DeleteModel(
            name='Cunstomer',
        ),
    ]
