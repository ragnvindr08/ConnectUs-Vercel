# Generated by Django 4.2.11 on 2024-06-08 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_comment_post_delete_usersettings_comment_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
