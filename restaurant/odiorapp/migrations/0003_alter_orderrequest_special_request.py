# Generated by Django 4.1.5 on 2024-08-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odiorapp', '0002_alter_orderrequest_special_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='special_request',
            field=models.TextField(blank=True, null=True),
        ),
    ]
