# Generated by Django 2.1.7 on 2019-05-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gthapp', '0003_auto_20190504_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('local_count', models.IntegerField(default=None, null=True)),
                ('global_count', models.IntegerField(default=None, null=True)),
                ('original', models.BooleanField(default=True)),
                ('rating', models.IntegerField(default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='originaltag',
            name='group',
        ),
        migrations.DeleteModel(
            name='OriginalTag',
        ),
        migrations.DeleteModel(
            name='OriginalTagsGroup',
        ),
        migrations.AddField(
            model_name='key',
            name='tags',
            field=models.ManyToManyField(to='gthapp.Tag'),
        ),
    ]
