# Generated by Django 5.1.7 on 2025-03-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Дедлайн'),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Низкий'), ('medium', 'Средний'), ('high', 'Высокий')], default='medium', max_length=10, verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Выполнено'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
