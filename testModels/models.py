from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')

class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男'), (1, '女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE,)
    #在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错：
    #TypeError: __init__() missing 1 required positional argument: 'on_delete'

class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版商名')
    location = models.CharField(max_length=30,verbose_name='地址')

class Book(models.Model):
    title = models.CharField(max_length=30,verbose_name='书名')
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)
