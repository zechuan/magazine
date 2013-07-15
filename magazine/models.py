#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.db import models
from markdown import markdown
import datetime
from django.contrib import admin

class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Journal(models.Model):
    volumn=models.CharField(max_length=20)
    introduce=models.CharField(max_length=200)
    journal_image=models.ImageField(upload_to="photos",max_length=200,blank=True, null=True)
    def __unicode__(self):
        return u"%s %s" % (self.volumn,self.introduce)
    class Meta:
        ordering=["volumn"]
        
    
class ArticleManager(models.Manager):
    """docstring for BlogManager"""
    def title_count(self, keyword):
        return self.filter(caption__icontains=keyword).count()
    def author_count(self, keyword):
        return self.filter(author__icontains=keyword).count()
    
VIEWABLE_STATUS = [3, 4]
class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager, self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Article(models.Model):
    """
    Aticle表示文章类
    """
    STATUES_CHOICES={
                     (1,"Needs Edit"),
                     (2,"Needs Approval"),
                     (3,"Published"),
                     (4,"Archived"),
                     }
    title=models.CharField(max_length=100)    #标题
    author = models.ForeignKey(Author)    #作者
    article_image=models.ImageField(upload_to="photos",max_length=200,blank=True, null=True)
    html_content = models.TextField(editable=False)    #html格式的页面文本
    markdown_content=models.TextField()    #markdown格式的页面正文
    journal_nom=models.ForeignKey(Journal)    #所属的期刊
    status=models.IntegerField(choices=STATUES_CHOICES,default=1)    #文章的状态，分为编辑、带发布、发布、归档
    publish_time = models.DateTimeField(auto_now_add=True)    #发表时间
    update_time = models.DateTimeField(auto_now=True)    #更新时间
    objects = models.Manager()
    count_objects = ArticleManager()
    
    def __unicode__(self):
        return u'%s %s %s' % (self.title, self.author, self.publish_time)
    
    class Meta:
        ordering=['update_time']
        
    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Article, self).save()

    admin_objects = models.Manager()
    objects = ViewableManager()

        
class catalog(models.Model):
    """
            用于存储期刊的文章排序
            有冗余
      """
    journal_nom=models.ForeignKey(Journal)
    article=models.ForeignKey(Article)
    indexinjournal=models.IntegerField()
    class Meta:
        ordering=['journal_nom']
        
