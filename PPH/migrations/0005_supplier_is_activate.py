# Generated by Django 4.2.3 on 2023-08-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PPH', '0004_alter_supplier_address_alter_supplier_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='is_activate',
            field=models.BooleanField(default=True),
        ),
    ]