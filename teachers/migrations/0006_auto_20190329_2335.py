# Generated by Django 2.1.7 on 2019-03-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_edulevel_teacherqualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='techer_id',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
    ]
