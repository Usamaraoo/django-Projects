# Generated by Django 3.0.3 on 2020-05-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(default='images/defaultProfile.jpg', upload_to='images/')),
                ('description_about_u', models.CharField(default='Who ARE YOU', max_length=1100)),
                ('skill', models.CharField(default='IT', max_length=200)),
                ('mail', models.CharField(default='None', max_length=200)),
                ('contact_no', models.CharField(blank=True, default='None', max_length=200)),
            ],
        ),
    ]
