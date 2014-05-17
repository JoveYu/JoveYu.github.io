<!--
.. title: [django]models中各种Field
.. slug: django-models-field
.. date: 2013-05-11T14:40:47+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

django.db.models是django中很重要的一层，处理着数据和对象的交换！在我看来，如果有SQL基础，学习这就很容易，因为基本上models就是将sql不同类型封装成了不同的类。

django入门后都知道models中有很多Field，其中很多Field为我们提供了便捷的功能，但是对于其中的各类Field掌握还不是很全，比如当时写博客问文章的Slug使用的是CharField后来还是小邪兽提醒我使用SlugField。今天通读了所有的Field就此也整理下

###AutoField
其实质是一个InterField，随着记录的增长自动增加，但是这个Field不需要我们太留心，因为如果你的models中没有primary key的时候就会自动添加一个AutoField

###BigIntegerField/SmallIntegerField
整型。。根据文档描述，BigIntegerField能表示-9223372036854775808到 9223372036854775807的数。

###BooleanField / NullBooleanField
布尔型，表示true or false 如果你希望他能够空，那么你需要用NullBooleanField

###CharField
字符串，没有什么好说的，比较常用，但是有一个必须赋值的参数max_length表示最大长度

###CommaSeparatedIntegerField
逗号分开的整形？实质是CharField，不是很理解

###DateField/DateTimeField/TimeField
日期和时间，类似python标准库中的datetime.date，其中有两个可选参数需要注意，auto\_now保存时自动使用当前时间，一般作为最后修改时间，auto\_now\_add新建对象时自动使用当前时间，一般作为创建时间！

###DecimalField
小数？英语不行，表示没看懂。

###EmailField
Email，本质应该是CharField加个验证Email的正则

###FileField / FilePathField
文件和文件路径，这块比较复杂，改天单独研究

###FloatField
浮点数，这个一般会和DecimalField混淆，但是本质是不同的一个使用python的float类型，一个使用的是Decimal

###ImageField
一个特殊的FileField，拥有两个额外的属性height_field,width_field

###IPAddressField
ip地址，这个真是比较特殊，以后省去自己判断，其中注意protocol默认是both也就是都接受，也可以单独设成'IPv4'或者'IPv6'表示只接受IPV4或者IPV6

###PositiveIntegerField/PositiveSmallIntegerField
非负整型

###SlugField
这个我特别喜欢，用来表示缩略表示内容，一般用来生成URL

###TextField
我个人认为这个和CharField类似，不同的仅仅是在form中这个需要TextArea,CharField仅仅需要TextInput

###URLField
URL，一般存储URL是django1.5中新加入的

