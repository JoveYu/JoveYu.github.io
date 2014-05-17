<!--
.. title: VC6调用AStyle
.. slug: vc6astyle
.. date: 2013-04-07T09:28:10+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

我也是在使用codeblocks后才知道了这样一个跨平台的小软件AStyle。
项目主页：http://astyle.sourceforge.net/

这个软件的主要作用是美化代码，调整缩进，我感觉的话，其实美化的还是蛮标准的，以前些的代码美化后还是耳目一新，那么在vc中怎么调用呢？

我经过尝试，分享下我的方法，在VC中点击[工具]（如果是英文版，类似），然后点击[定制]，打开[工具]选项卡，可以看到这样的界面


点击新建，名字就写AStyle，选择astyle的路径，变量填

>--style=ansi --indent=spaces=4 -M80 -k1 -p -j -D -H -c -w $(FileName)$(FileExt)

目录填$(FileDir)

这样就行啦

