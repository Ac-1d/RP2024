# Generated by Django 3.2 on 2024-06-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0008_auto_20240603_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel_chapter',
            name='chapter_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='novel_chapter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
