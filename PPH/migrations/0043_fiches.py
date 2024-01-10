# Generated by Django 4.2.3 on 2024-01-10 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PPH', '0042_demandes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attente_controle', models.BooleanField(default=False)),
                ('prep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PPH.formule')),
            ],
        ),
    ]
