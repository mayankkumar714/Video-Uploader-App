# Generated by Django 2.2.4 on 2019-09-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20190918_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='desciption',
            field=models.CharField(default='Action', max_length=500),
        ),
    ]
