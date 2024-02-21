# Generated by Django 5.0.2 on 2024-02-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_rename_checkout1_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('town_city', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('apartment', models.CharField(blank=True, max_length=255, null=True)),
                ('postcode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('user_id', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('products', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
    ]
