# Generated by Django 4.2.17 on 2025-01-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
