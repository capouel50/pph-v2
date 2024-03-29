# Generated by Django 4.2.3 on 2024-01-01 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PPH', '0034_parametresformules'),
    ]

    operations = [
        migrations.AddField(
            model_name='formule',
            name='agiter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formule',
            name='contre_indications',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='formule',
            name='duree',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formule',
            name='froid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formule',
            name='liste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PPH.liste'),
        ),
        migrations.AddField(
            model_name='formule',
            name='lumiere',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formule',
            name='mode_operatoire',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='formule',
            name='publications',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='formule',
            name='voie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PPH.voie'),
        ),
    ]
