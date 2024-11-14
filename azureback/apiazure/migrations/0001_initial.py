# Generated by Django 4.2.16 on 2024-11-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=250, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('isadmin', models.BooleanField(default=False)),
                ('imagefield', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
    ]
