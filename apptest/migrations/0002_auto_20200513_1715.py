# Generated by Django 3.0.5 on 2020-05-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcasestep',
            name='apptestresult',
            field=models.BooleanField(verbose_name='测试结果'),
        ),
    ]
