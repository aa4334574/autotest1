# Generated by Django 3.0.5 on 2020-04-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20200422_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apistep',
            old_name='apitestname',
            new_name='apiname',
        ),
        migrations.RemoveField(
            model_name='apitest',
            name='Product',
        ),
        migrations.AddField(
            model_name='apistep',
            name='apistep',
            field=models.CharField(max_length=100, null=True, verbose_name='测试步骤'),
        ),
    ]
