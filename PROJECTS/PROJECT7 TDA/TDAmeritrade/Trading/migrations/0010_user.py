# Generated by Django 2.2.1 on 2021-04-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trading', '0009_auto_20200618_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('permission', models.CharField(default='admin', max_length=20)),
            ],
        ),
    ]
