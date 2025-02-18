# Generated by Django 4.2.16 on 2025-02-16 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('isactive', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=250, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('isadmin', models.BooleanField(default=False)),
                ('imagefield', models.ImageField(default=None, upload_to='images/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bscale', models.DateTimeField()),
                ('escale', models.DateTimeField()),
                ('max_particpant', models.PositiveIntegerField(default=10)),
                ('max_voluntary_per_horary', models.PositiveIntegerField()),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('banner', models.ImageField(upload_to='banners/')),
            ],
        ),
        migrations.CreateModel(
            name='Horary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('max_voluntary_scale', models.PositiveBigIntegerField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('msg', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voluntary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uservoluntary', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apiazure.event')),
                ('horarys', models.ManyToManyField(db_index=True, related_name='horaryvoluntary', to='apiazure.horary')),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiazure.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiazure.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='horary',
            name='voluntarys',
            field=models.ManyToManyField(related_name='voluntarylist', to='apiazure.voluntary'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='participants',
            constraint=models.UniqueConstraint(fields=('user', 'event'), name='unique_user_event'),
        ),
        migrations.AddField(
            model_name='follow',
            name='organizator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apiazure.organization'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apiazure.organization'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('organizator', 'user'), name='unique_follow'),
        ),
    ]
