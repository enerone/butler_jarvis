# Generated by Django 3.1.3 on 2020-11-30 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201129_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click the link above to Blog', max_length=255),
        ),
    ]
