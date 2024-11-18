# Generated by Django 4.2.16 on 2024-11-18 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiazure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeDate', models.DateTimeField()),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('banner', models.ImageField(upload_to='banners/')),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
