# Generated by Django 2.2.1 on 2021-04-29 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trading', '0012_auto_20210429_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategy',
            name='user_id',
        ),
        migrations.AddField(
            model_name='strategy',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='strategy_user', to='Trading.User'),
        ),
    ]
