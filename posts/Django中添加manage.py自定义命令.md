<!--
.. title: Django中添加manage.py自定义命令
.. slug: django-add-managepy
.. date: 2013-05-04T11:54:52+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

最近一直忙着寻找实习，也没什么时间来学习新的知识，越找啊越觉得自己懂得东西少。现在安顿下来，也要静下心来学习了！

manage.py是django的管理文件，简单的来说也可以理解为一个总控制台，我们日常操作django都可以通过他，比如我们需要启动调试服务器，我们会用到这样的命令：

>python2 manage.py runserver

runserver就是其中一个管理命令，那么我们现在来尝试下自己添加管理命令。有人可能会这样认为管理嘛干嘛一定要在这里添加命令，自己写个脚本不就可以了，我是这样理解的，每个app都有自己的功能，如果需要一些自定义的功能的时候这样分类方便，将命令写入app也有助于以后app的重构。

再来个通俗点的，规范总是有价值的，不知道为什么那么遵守就是!开个玩笑！

我们先创建一个以命令名称为文件名的py文件，例如mycommand.py写入类似下面的代码：

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    args='any args'
    help='print hello world'

    def handle(self,*args,**options):
        print 'hello world'
```

简单的来说就是继承BaseCommand来实现我们需要的功能，这里args指的是参数，但是并不影响你的输入，仅作为帮助提示，help顾名思义帮助文档，类似\__doc__主要显示这条命令的功能，当然这两个参数可以不写的，主要就是其中的handle函数，这个函数完成这条命令的主体功能！

完成这些后将这个文件放入你的app的management/commands目录下目录结构应该是这样的

```bash
├── __init__.py
├── management
│   ├── commands
│   │   ├── __init__.py
│   │   └── mycommand.py
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

这样django就会自动识别这些命令了，记得要启用你的app哦。这个时候我们运行

>python2 manage.py

你应该可以看到他提示你的命令了

>[myapp]   
>    mycommand

现在我们看看提示

```bash
$ python2 manage.py help mycommand
Usage: manage.py mycommand [options] any args

print hello world
```

然后运行试试
```bash
$ python2 manage.py mycommand     
hello world
```
一个简单的例子就这样完成了，再使用时，好好考虑那些功能需要做成manage.py的命令，比如我准备写个简单的命令，将博客文章导出成markdown文件，做个备份