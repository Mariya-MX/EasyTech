# Generated by Django 4.2.5 on 2023-11-30 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_remove_booking_work_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.booking')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.technicianprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
