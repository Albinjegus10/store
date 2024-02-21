# Generated by Django 5.0.1 on 2024-02-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_yorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rtitle', models.CharField(max_length=255)),
                ('Rimage', models.ImageField(blank=True, null=True, upload_to='categories/')),
                ('Rprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('click_count', models.IntegerField(default=0)),
                ('return_status', models.CharField(choices=[('Return Order', 'Return Order'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('Request Approved', 'Request Approved'), ('On Hold', 'On Hold')], default='Return Order', max_length=50)),
            ],
        ),
    ]
