<!--
.. title: django-south使用，维护利器
.. slug: django-south
.. date: 2013-04-08T14:50:27+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

django网站数据库方便基本上都是自动维护的，但是如果要修改数据库就会比较麻烦，查了下相关的文档，django通过syncdb无法实现对models的增加。因为可能会造成意外的错误，所以推介手动修改数据库。但是比如我这个blog的维护，加入新功能难免会修改数据库，这里介绍个便捷的方法使用django-south

大家可以上他们[官网](http://south.aeracode.org/)来获取包的最新版本，也可以通过pip安装

下面简单讲下这个包的使用

 1. 在INSTALL_APP中添加south，通过syncdb将south同步进数据库
 
 2. 执行下列这个句，在你的app目录下创建migrations目录以及第一次迁移需要的0001_initial.py文件
>python2 manage.py convert_to_south youappnam

 3. 如果models改变就执行
>python2 manage.py schemamigration youappname --auto

 4. 最后执行同步数据库（如果出现表已存在的错误，后面加 --fake）
>migrate manage.py youappnam 