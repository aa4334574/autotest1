from django.db import models
from product.models import Product
# Create your models here.

class Bug(models.Model):
    Product = models.ForeignKey('product.Product',on_delete = models.CASCADE,null = True)
    bugname = models.CharField('Bug名称',max_length = 64)#bug名称
    bugdetail = models.CharField('Bug详情',max_length = 200)#详情
    BUG_STATUS = (('激活','激活'),('已解决','已解决'),('已关闭','已关闭')) # verbose_name admin账号中显示的名称
    bugstatus = models.CharField(verbose_name = '解决状态',choices = BUG_STATUS,default = '激活',max_length = 10,null = True)#解决状态
    BUG_LEVAL = (('1','1'),('2','2'),('3','3'))
    bug_leval = models.CharField(verbose_name = '严重程度',choices = BUG_LEVAL,default = '3',max_length = 10,null = True)#严重程度
    bugcreater = models.CharField('创建人',max_length = 20)#创建人
    bugassign = models.CharField('指派给',max_length = 20)#指派人
    create_time = models.DateTimeField('创建时间',auto_now_add = True)#创建时间
    update_time = models.DateTimeField('更新时间',auto_now = True)#更新时间
    class Meta:
        """
        地址表的内容行为，例如现在该表定义为Bug管理
        """
        verbose_name = 'Bug管理'#定义中文表名
        verbose_name_plural = 'Bug管理'#复数形式
    def __str__(self):
        return self.bugname
