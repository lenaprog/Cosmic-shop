# Generated by Django 4.0.1 on 2022-04-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0004_remove_article_image_link_alter_article_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]