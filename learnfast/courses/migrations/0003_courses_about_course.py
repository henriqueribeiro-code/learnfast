# Generated by Django 3.1.4 on 2020-12-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201204_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='about_course',
            field=models.TextField(blank=True, verbose_name='About Course'),
        ),
    ]
