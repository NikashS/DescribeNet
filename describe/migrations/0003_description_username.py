# Generated by Django 2.2.10 on 2021-01-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('describe', '0002_description_class_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='username',
            field=models.CharField(default='beforenamed', max_length=200),
            preserve_default=False,
        ),
    ]
