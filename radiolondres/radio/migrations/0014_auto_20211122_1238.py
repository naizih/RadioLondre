# Generated by Django 3.2.6 on 2021-11-22 12:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0013_action_resistant_has_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='message_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='radio.message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date, null=True),
        ),
        migrations.AlterField(
            model_name='posteradio',
            name='StudioRadio_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.studioradio'),
        ),
        migrations.AlterField(
            model_name='posteradio',
            name='messageCourant_text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='resistant',
            name='studioRadio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.studioradio'),
        ),
        migrations.AlterField(
            model_name='resistant_has_message',
            name='message_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.message'),
        ),
        migrations.AlterField(
            model_name='resistant_has_message',
            name='resistant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.resistant'),
        ),
        migrations.AlterField(
            model_name='studioradio',
            name='messageCourant_text',
            field=models.CharField(max_length=255),
        ),
    ]
