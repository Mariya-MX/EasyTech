# Generated by Django 4.2.5 on 2023-11-15 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='technician_availability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.technicianavailability'),
        ),
    ]
