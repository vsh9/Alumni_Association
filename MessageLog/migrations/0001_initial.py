# Generated by Django 5.1 on 2024-08-24 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumni', '0003_alter_alumni_phone_number'),
        ('Notifications', '0002_alter_notification_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='ML',
            fields=[
                ('ml_id', models.AutoField(primary_key=True, serialize=False)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_status', models.CharField(choices=[('sent', 'Sent'), ('failed', 'Failed')], max_length=20)),
                ('response_status', models.CharField(choices=[('read', 'Read'), ('unread', 'Unread')], default='unread', max_length=20)),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumni.alumni')),
                ('n_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notifications.notification')),
            ],
        ),
    ]
