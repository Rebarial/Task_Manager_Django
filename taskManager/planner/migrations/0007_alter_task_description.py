# Generated by Django 5.0.3 on 2024-03-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default=0, verbose_name='Description'),
            preserve_default=False,
        ),
    ]
