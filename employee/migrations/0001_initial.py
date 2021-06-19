# Generated by Django 3.2.3 on 2021-06-19 05:55

from django.db import migrations, models
import employee.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=500)),
                ('salary', models.CharField(max_length=20)),
                ('joining_date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('account_holder_name', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=50)),
                ('MCIR_code', models.CharField(max_length=50)),
                ('IFSC_code', models.CharField(max_length=50)),
                ('name_of_bank', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to=employee.models.employee_upload_to)),
            ],
        ),
    ]
