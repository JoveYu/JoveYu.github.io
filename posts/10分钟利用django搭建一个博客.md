<!--
.. title: 10分钟利用django搭建一个博客
.. slug: 10django
.. date: 2013-04-07T10:11:50+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

以前老是听说ROR开发有多快多块，网上还有朋友为了证明这，专门制作了10分钟利用rails框架搭建一个简易博客的教程，最近学习django框架，觉得django给开发者的便捷也很多，心血来潮来写个10分钟用django搭建简易博客的教程。

## 写在文章前

我不是什么web高手，接触web不久，正努力往大神的方向追赶，高手看到这的时候可以去喝咖啡了！10分钟不能完成博客的全部功能，只能完成博客最基本的显示文章和标题的功能，如果大家有兴趣可以慢慢去完善，比如评论，RSS。界面上大家凑合看吧！哈哈。

我写这篇文章的时候使用的python2.7,django1.4,如果版本不一样的话相信也区别不大，个别参数或者路径不同罢了！下面的代码多用于linux，windows下区别不大稍微修改点就好！

## 建立项目
看到这里，就是假定你已经安装好了python和django了！这些问题相信官方文档能帮助你更多！

	:::bash
	django-admin.py startproject mysite

我们会得到这样的文件结构

	:::bash
	mysite
	├── manage.py
	└── mysite
	    ├── __init__.py
	    ├── settings.py
	    ├── urls.py
	    └── wsgi.py

编辑settings.py里DATABASES项如下

	:::python
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': '/home/jove/mydb.md',    # Or path to database file if using sqlite3.
		'USER': '',                      # Not used with sqlite3.
		'PASSWORD': '',                  # Not used with sqlite3.
		'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	    }
	}

这里数据库我选的sqlite方便，单文件，别的数据库也可以，填写方法类似，顺便说句，windows平台，我记得路径不同要填为

	:::python
	r'C:\py\mydb.md'


然后在主目录为项目添加一个app，这里我们命名为myblog

	:::bash
	python2 manage.py startapp myblog

这时我们就可以看到目录中建立的app了

## 构建数据库
修改myblog/modesl.py加入如下内容，

	:::python
	from django.db import models
	from django.contrib import admin

	class Blog(models.Model):
	    title=models.CharField(max_length=120)
	    body=models.TextField()
	    time=models.DateTimeField()

	class BlogAdmin(admin.ModelAdmin):
	    list_display=('title','time')

	admin.site.register(Blog,BlogAdmin)

在settings.py中的INSTALLED_APPS中添加

	:::python
	'myblog',
	'django.contrib.admin',

修改urls.py为如下样式，只用删除几个注释即可

	:::python
	from django.conf.urls import patterns, include, url
	from django.contrib import admin
	admin.autodiscover()

	urlpatterns = patterns('',
	    url(r'^admin/', include(admin.site.urls)),
	)

然后让django自动构建数据库，利用下面这一条命令

	:::python
	python2 manage.py syncdb

过程中会提示你创建管理员帐号，根据提示创建就好！

## 构造页面

基本上这个时候博客的功能就算完成了，但是在哪里显示呢，所以我们要构建一个前台页面，简单的博客，我们就用一个单页面完成！
在myblog文件夹里创建文件夹templates里面存放这我们要的模板，顺便建立一个模板叫archive.html内容如下

	:::django
	<html>
	<style type="text/css">
	body{color:#efd;background:#453;padding:0 5em;margin:0}
	h1{padding:2em 1em;background:#675}
	h2{color:#bf8;border-top:1px dotted #fff;margin-top:2em}
	p{margin:len 0}
	</style>
	<body>
	<h1>my blog</h1>
	{% for post in posts %}
	<h2>{{post.title}}</h2>
	<p>{{post.time}}</p>
	<p>{{post.body}}</p>
	{% endfor %}
	</body>
	</html>

其中一个for循环就用来依次显示文章

然后我们创建一个视图函数编辑myblog/views.py如下

	:::python
	from django.template import loader,Context
	from django.http import HttpResponse
	from myblog.models import Blog

	def archive(request):
	    posts=Blog.objects.all()
	    t=loader.get_template("archive.html")
	    c=Context({'posts':posts})
	    return HttpResponse(t.render(c))


接着处理首页的关联函数，编辑urls.py导入前面定义的函数并关联到主页，添加

	:::python
	from myblog.views import archive
	urlpatterns = patterns('',
	    url(r'^$', archive),
	#......



## 运行测试
django自带开发服务器，方便了很多，只需要运行

	:::bash
	python2 manage.py runserver

得到这样的显示

>0 errors found    
>Django version 1.4.2, using settings 'mysite.settings'  
>Development server is running at http://127.0.0.1:8000/  
>Quit the server with CONTROL-C.  

然后在浏览器中打开后台http://127.0.0.1:8000/admin你们应该看到的是这样子的
![1](http://jovesky4django-uploads.stor.sinaapp.com/2013/04/DeepinScrot-2651.png)

在blog中add添加然后可以看到简洁的文章输入界面，是不是有一点博客的味道了，呵呵，试试添加几篇文章，然后在首页去查看

![2](http://jovesky4django-uploads.stor.sinaapp.com/2013/04/DeepinScrot-2900.png)

到这里我们的教程就结束了。写的比较急，如果有错误还请指出！