# Generated by Django 4.2.3 on 2023-09-12 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PPH', '0014_forme_typematiere_unitemesure_matierepremiere_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='matierepremiere',
            name='liste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PPH.liste'),
        ),
    ]
