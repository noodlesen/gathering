# Generated by Django 2.1.7 on 2019-05-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthapp', '0007_auto_20190511_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='keys',
            field=models.ManyToManyField(blank=True, null=True, to='gthapp.Key'),
        ),
    ]