# Generated by Django 2.2.2 on 2019-07-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='teaser',
            field=models.CharField(max_length=500),
        ),
    ]