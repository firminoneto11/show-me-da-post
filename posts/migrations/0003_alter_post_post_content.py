# Generated by Django 3.2.6 on 2021-08-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_user_id_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(blank=True, max_length=255, verbose_name='Content'),
        ),
    ]
