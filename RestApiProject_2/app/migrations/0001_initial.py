# Generated by Django 3.0.3 on 2020-04-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('published', models.DateField()),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to='covers/')),
            ],
        ),
    ]
