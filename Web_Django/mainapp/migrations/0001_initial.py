# Generated by Django 4.0.1 on 2023-06-20 03:43

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phon', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_num', models.IntegerField(primary_key=True, serialize=False)),
                ('cate_name', models.CharField(max_length=100, unique=True)),
                ('cate_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'CATEGORY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_num', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('comment_create_date', models.DateTimeField(auto_now_add=True)),
                ('comment_modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'COMMENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('com_num', models.AutoField(primary_key=True, serialize=False)),
                ('cate_name', models.CharField(max_length=255)),
                ('com_title', models.CharField(max_length=255)),
                ('com_content', models.TextField()),
                ('com_combool', models.CharField(max_length=1)),
                ('com_date', models.DateTimeField(auto_now_add=True)),
                ('com_count', models.IntegerField(default=1)),
                ('com_path', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Community',
                'managed': False,
            },
        ),
    ]
