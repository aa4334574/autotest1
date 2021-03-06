from django.db import models
from product.models import Product

class Webcase(models.Model):
    Product = models.ForeignKey('product.Product',on_delete = models.CASCADE,null = True)#关联产品id
    webcasename = models.CharField('用例名称',max_length = 200) #测试用例名称
    webtestresult  = models.BooleanField('测试结果')
    webtester = models.CharField('测试负责人',max_length = 20) #测试负责人
    createtime = models.DateTimeField('创建时间',auto_now_add = True)#创建时间
    updatetime = models.DateTimeField('更新时间',auto_now=True)#更新时间

    class Meta:
        verbose_name = 'web测试用例'
        verbose_name_plural = 'web测试用例'
    def __str__(self):
        return self.webcasename

class Webcasestep(models.Model):
    Webcase = models.ForeignKey('Webcase',on_delete=models.CASCADE) # 关联接口ID
    # webcasename = models.CharField('测试用例标题',max_length=200) # 测试用例标题
    webteststep = models.CharField('测试步骤',max_length=200) # 测试步骤
    webtestobjname = models.CharField('测试对象名称描述',max_length=200) # 测试对象名称描述
    webfindmethod = models.CharField('定位方式',max_length=200) # 定位方式
    webevelement = models.CharField('控件元素',max_length=800) # 控件元素
    weboptmethod = models.CharField('操作方法',max_length=200) # 操作方法
    webtestdata = models.CharField('测试数据',max_length=200,null=True) # 测试数据，临时增加字段时要设置可为空
    webassertdata = models.CharField('验证数据',max_length=200) # 验证数据
    webtestresult = models.BooleanField('测试结果') # 测试结果
    createtime = models.DateTimeField('创建时间',auto_now_add=True) # 创建时间-自动获取当前时间
    updatetetime = models.DateTimeField('更新时间',auto_now=True)
    def __str__(self):
        return self.webteststep
# Create your models here.
