# Generated by Django 3.2.9 on 2021-12-03 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post_userpostlikestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]