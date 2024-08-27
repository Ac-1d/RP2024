# Generated by Django 3.2 on 2024-08-22 02:01

import apps.novels.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('novels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recently_reading',
            name='user',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recently_user', to='users.user', verbose_name='用户外键'),
        ),
        migrations.AddField(
            model_name='novel_list',
            name='Novel',
            field=models.ForeignKey(db_constraint=apps.novels.models.Novel, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Novel_list', to='novels.novel', verbose_name='小说外键'),
        ),
        migrations.AddField(
            model_name='novel_list',
            name='user',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='users.user', verbose_name='用户外键'),
        ),
        migrations.AddField(
            model_name='novel_chapter',
            name='novel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Novel', to='novels.novel', verbose_name='小说外键'),
        ),
        migrations.AddField(
            model_name='novel',
            name='author',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Novel', to='novels.author', verbose_name='小说作者'),
        ),
        migrations.AddField(
            model_name='novel',
            name='category',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='novel_category', to='novels.novel_category', verbose_name='小说分类'),
        ),
        migrations.AddField(
            model_name='comment',
            name='chapter',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter_comments', to='novels.novel_chapter'),
        ),
        migrations.AddField(
            model_name='comment',
            name='novel',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='novel_comments', to='novels.novel'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.user'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='novel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novels.novel', verbose_name='小说'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='novel_chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novels.novel_chapter', verbose_name='章节'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='author',
            name='author_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='author', to='users.user'),
        ),
        migrations.AlterUniqueTogether(
            name='novel_chapter',
            unique_together={('novel', 'chapter_id')},
        ),
    ]
