# Generated by Django 4.0.4 on 2022-06-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='registration',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
