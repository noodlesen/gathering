# Generated by Django 2.1.7 on 2019-05-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthapp', '0004_auto_20190506_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='footage',
            name='shortcode',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='tags',
            field=models.ManyToManyField(blank=True, to='gthapp.Tag'),
        ),
    ]
