# Generated by Django 3.2.6 on 2021-11-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0016_auto_20211122_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaboteurFerroviaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=25)),
                ('groupeClandestin_id', models.ManyToManyField(to='radio.GroupeClandestin')),
            ],
        ),
    ]
