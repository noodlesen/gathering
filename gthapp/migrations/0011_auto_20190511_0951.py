# Generated by Django 2.1.7 on 2019-05-11 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gthapp', '0010_remove_author_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gthapp.Author'),
        ),
        migrations.AddField(
            model_name='post',
            name='footage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gthapp.Footage'),
        ),
        migrations.AlterField(
            model_name='author',
            name='group',
            field=models.ManyToManyField(blank=True, to='gthapp.UsersGroup'),
        ),
    ]