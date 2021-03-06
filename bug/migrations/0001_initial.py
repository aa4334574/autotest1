# Generated by Django 3.0.5 on 2020-04-28 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bugname', models.CharField(max_length=64, verbose_name='Bug名称')),
                ('bugdetail', models.CharField(max_length=200, verbose_name='Bug详情')),
                ('bugstatus', models.CharField(choices=[('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭')], default='激活', max_length=10, null=True, verbose_name='解决状态')),
                ('bug_leval', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='3', max_length=10, null=True, verbose_name='严重程度')),
                ('bugcreater', models.CharField(max_length=20, verbose_name='创建人')),
                ('bugassign', models.CharField(max_length=20, verbose_name='指派给')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'Bug管理',
                'verbose_name_plural': 'Bug管理',
            },
        ),
    ]
