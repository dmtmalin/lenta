# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('published', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('link', models.URLField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
            ],
            options={
                'ordering': ('-published',),
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0420\u0443\u0431\u0440\u0438\u043a\u0430',
                'verbose_name_plural': '\u0420\u0443\u0431\u0440\u0438\u043a\u0438',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digest.Rubric', verbose_name='\u0420\u0443\u0431\u0440\u0438\u043a\u0430'),
        ),
    ]
