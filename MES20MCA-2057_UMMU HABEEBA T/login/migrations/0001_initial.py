# Generated by Django 3.0.8 on 2022-06-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('u_id', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
