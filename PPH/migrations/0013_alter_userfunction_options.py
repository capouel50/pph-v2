# Generated by Django 4.2.3 on 2023-08-28 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PPH', '0012_alter_customuser_function'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfunction',
            options={'ordering': ['title']},
        ),
    ]
