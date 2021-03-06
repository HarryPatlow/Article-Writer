# Generated by Django 4.0 on 2022-03-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_url_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
