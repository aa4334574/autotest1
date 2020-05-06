from django.db import models

class Appcase(models.Model):
    Product =models.ForeignKey('product.Product',on_delete = models.CASCADE,null=True)#关联产品的外部id
    appcasename = models.CharField('用例名称',max_length = 200)#app用例名称
    apptestresult = models.BooleanField('测试结果')#测试结果
    apptester = models.CharField('测试负责人',max_length=10)#测试负责人
    create_time = models.DateTimeField('创建时间',auto_now_add=True)#创建时间
    update_time = models.DateTimeField('更新时间',auto_now=True)#更新时间
    class Meta:
        verbose_name='app测试用例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.appcasename


class Appcasestep(models.Model):
    Appcase = models.ForeignKey(Appcase,on_delete=models.CASCADE,null=True)#关联appcase的外部id
    appteststep = models.CharField('测试步骤',max_length= 300)#app测试步骤
    apptestobjname = models.CharField('测试对象名称描述',max_length=300)#测试对象的名称描述
    appfindmethod = models.CharField('定位方式',max_length = 500)#定位方式
    appevelement = models.CharField('控件元素',max_length = 200)#控件元素
    appoptmethod = models.CharField('操作方法',max_length = 200)#操作方法
    apptestdata = models.CharField('测试数据',max_length = 300)#测试数据
    appassertdata = models.CharField('断点数据',max_length = 300)#断点数据
    apptestresult = models.CharField('测试结果',max_length= 200)#测试结果
    create_time = models.DateTimeField('创建时间',auto_now_add = True)
    updata_time = models.DateTimeField('更新时间',auto_now = True)
    def __str__(self):
        return self.appteststep
# Create your models here.
