# Generated by Django 4.2.2 on 2023-06-21 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_seriesnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='posting_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 6, 21)),
        ),
    ]
