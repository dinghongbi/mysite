from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版社名称')
    address = models.CharField(max_length=50,verbose_name='出版社地址')
    city = models.CharField(max_length=60,verbose_name='城市')
    state_province = models.CharField(max_length=30,verbose_name='省会')
    country = models.CharField(max_length=50,verbose_name='国家')
    website = models.URLField(blank=True,verbose_name='网站')

    def __unicode__(self):
    	return self.name
    def __str__(self):
    	return self.name

    class Meta:
    	ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='姓')
    last_name = models.CharField(max_length=40,verbose_name='名')
    email = models.EmailField(blank=True,verbose_name='e-mail')

    def _unicode_(self):
    	return u'%s %s'%(self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100,verbose_name='书名')
    authors = models.ManyToManyField(Author,verbose_name='作者')
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,verbose_name='出版社')
    publication_date = models.DateField('出版日期',blank=True,null=True)

    def __unicode__(self):
    	return self.title