# Generated by Django 4.2.5 on 2024-04-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0098_delete_bookingdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('availability_id', models.IntegerField()),
                ('technician_id', models.IntegerField()),
                ('user_email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=20)),
            ],
        ),
    ]
