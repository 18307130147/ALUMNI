# Generated by Django 3.2.5 on 2021-07-12 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0006_activity_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tie',
            name='tag',
        ),
        migrations.AddField(
            model_name='tie',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.tag', verbose_name='所属标签'),
        ),
    ]
