# Generated by Django 4.1.2 on 2022-11-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(height_field='height_field', upload_to='user_directory_path', width_field='width_field'),
        ),
    ]