# Generated by Django 3.2.6 on 2021-11-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0004_alter_message_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
