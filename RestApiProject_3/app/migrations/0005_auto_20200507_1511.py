# Generated by Django 3.0.3 on 2020-05-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200507_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='published',
            new_name='created_date',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='description',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='price',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='title',
        ),
        migrations.AddField(
            model_name='questions',
            name='question',
            field=models.CharField(default='enter Question', max_length=50, unique=True),
        ),
    ]
