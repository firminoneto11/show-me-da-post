# Generated by Django 3.2.6 on 2021-08-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(max_length=255, verbose_name='Content'),
        ),
    ]
