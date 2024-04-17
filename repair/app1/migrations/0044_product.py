# Generated by Django 4.2.5 on 2024-02-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0043_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('ad_title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
