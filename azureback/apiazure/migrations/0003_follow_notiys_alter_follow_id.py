# Generated by Django 4.2.16 on 2025-02-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiazure', '0002_alter_follow_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='notiys',
            field=models.ManyToManyField(to='apiazure.notify'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
