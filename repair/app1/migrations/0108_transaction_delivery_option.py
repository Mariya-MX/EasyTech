# Generated by Django 4.2.5 on 2024-04-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0107_remove_transaction_refunded'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='delivery_option',
            field=models.BooleanField(default=False),
        ),
    ]
