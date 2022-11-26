# Generated by Django 4.1.2 on 2022-11-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_height_field_posts_width_field_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-id', 'timestamp', 'updated'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(height_field='height_field', upload_to='images/', width_field='width_field'),
        ),
    ]