# Generated by Django 4.0.3 on 2022-04-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_group',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2),
        ),
    ]
