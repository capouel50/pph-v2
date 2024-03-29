# Generated by Django 4.2.3 on 2023-09-12 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PPH', '0013_alter_userfunction_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMatiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UniteMesure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MatierePremiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('fournisseur', models.CharField(max_length=250)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prix_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qté_stock', models.PositiveIntegerField()),
                ('stock_mini', models.PositiveIntegerField()),
                ('liste', models.TextField()),
                ('stockee', models.BooleanField(default=False)),
                ('forme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PPH.forme')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PPH.typematiere')),
            ],
        ),
        migrations.AddField(
            model_name='forme',
            name='unite_mesure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PPH.unitemesure'),
        ),
    ]
