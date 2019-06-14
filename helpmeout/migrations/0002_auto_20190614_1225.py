# Generated by Django 2.2.2 on 2019-06-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpmeout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesstoken',
            name='oauth_token',
            field=models.CharField(default='default', max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='ot_secret',
            field=models.CharField(default='default', max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user_id',
            field=models.CharField(default='default', max_length=100000),
            preserve_default=False,
        ),
    ]