# Generated by Django 2.2.1 on 2020-06-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trading', '0005_auto_20200616_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_id', models.IntegerField(default=1)),
                ('order_id', models.IntegerField(default=0)),
                ('order_type', models.CharField(max_length=20)),
                ('price', models.FloatField(default=0)),
                ('duration', models.CharField(max_length=20)),
                ('instruction', models.CharField(max_length=20)),
                ('quantity', models.FloatField(default=1)),
                ('symbol', models.CharField(max_length=20)),
                ('asset_type', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('time', models.IntegerField(default=0)),
            ],
        ),
    ]
