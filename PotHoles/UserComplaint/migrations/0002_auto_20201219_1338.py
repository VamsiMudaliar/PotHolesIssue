# Generated by Django 3.0.8 on 2020-12-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserComplaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addissue',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
