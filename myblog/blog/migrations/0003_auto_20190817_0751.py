# Generated by Django 2.1.1 on 2019-08-16 23:51

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190816_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
    ]
