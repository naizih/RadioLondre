# Generated by Django 3.2.6 on 2021-11-09 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0010_alter_groupeclandestin_posteradio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envahisseur',
            name='PosteRadio_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='radio.posteradio'),
        ),
    ]
