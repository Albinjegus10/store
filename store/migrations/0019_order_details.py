# Generated by Django 5.0.1 on 2024-02-01 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_offers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('town_city', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('apartment', models.CharField(blank=True, max_length=255, null=True)),
                ('postcode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('ship_to_different_address', models.BooleanField(default=False)),
                ('order_notes', models.TextField(blank=True, null=True)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=50, null=True)),
                ('payment_method', models.CharField(choices=[('paypal', 'Paypal'), ('gpay', 'Google Pay'), ('phonepe', 'PhonePe'), ('cash', 'Cash On Delivery')], max_length=255)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productmaster')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.userprofile')),
            ],
            options={
                'db_table': 'store_Order_details',
            },
        ),
    ]
