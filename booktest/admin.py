# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *
# Register your models here.
# 关联对象增加快捷方式
class HeroInfoInline( admin.TabularInline): #admin.StackedInline
    model = HeroInfo
    extra = 3




# 添加显示式样
class BookInfoAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ['id','btitle','bput_date']
    # 过滤
    list_filter = ['btitle']
    # 查找
    search_fields = ['btitle']
    # 分页（每页有几条）
    list_per_page = 10
#     属性的先后顺序
#     fields = ['bput_date','btitle']
#     属性分组
    fieldsets = [
        ('basic',{'fields':['btitle']}),
        ('super',{'fields':['bput_date']})
    ]
    inlines = [HeroInfoInline]



admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)