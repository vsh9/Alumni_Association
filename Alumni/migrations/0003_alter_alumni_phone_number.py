# Generated by Django 5.1 on 2024-08-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0002_rename_address_alumni_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='phone_number',
            field=models.IntegerField(default=1234, max_length=10),
            preserve_default=False,
        ),
    ]
