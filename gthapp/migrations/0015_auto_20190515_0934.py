# Generated by Django 2.1.7 on 2019-05-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthapp', '0014_auto_20190513_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footage',
            name='path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]