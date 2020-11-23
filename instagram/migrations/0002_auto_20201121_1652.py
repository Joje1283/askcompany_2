# Generated by Django 3.1.2 on 2020-11-21 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='instagram/post/%Y/%m/%d'),
        ),
    ]