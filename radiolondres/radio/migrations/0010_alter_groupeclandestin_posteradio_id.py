# Generated by Django 3.2.6 on 2021-11-09 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0009_alter_action_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupeclandestin',
            name='PosteRadio_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='radio.posteradio'),
        ),
    ]
