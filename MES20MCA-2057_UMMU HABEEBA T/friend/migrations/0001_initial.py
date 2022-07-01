# Generated by Django 3.0.8 on 2022-06-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30)),
                ('f_mobile', models.CharField(max_length=30)),
                ('f_mail', models.CharField(max_length=50)),
                ('f_gender', models.CharField(max_length=30)),
                ('f_dob', models.DateField()),
                ('f_location', models.CharField(max_length=30)),
                ('f_uname', models.CharField(max_length=30)),
                ('f_pass', models.CharField(max_length=30)),
                ('f_profile_pic', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'friend',
            },
        ),
    ]
