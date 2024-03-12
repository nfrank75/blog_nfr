# Generated by Django 4.2.11 on 2024-03-12 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_category_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_blog.category'),
            preserve_default=False,
        ),
    ]
