<!--
.. title: Linux下chrome的字体设置
.. slug: linuxchrome1
.. date: 2013-04-07T09:10:54+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

试了好多种方法，通过浏览器Preference中设置，字体看着总是那么别扭，安装了插件Change Font虽然可以使用，可是强制将字体全部更改总感觉不太爽，况且效果不是很好。试了下面这种方法，效果不错

编辑~/.config/google-chrome/Default/User StyleSheets/Custom.css文件

添加如下几行：

	:::css
	@charset "utf-8";
	body * {
	font-family:"WenQuanYi Micro Hei","wqy-microhei",Tahoma,SimSun !important;
	}


再分享一个我的设置

	:::css
	@charset "utf-8";
	body * {
	font-family:"Microsoft YaHei",SimSun,Tahoma,"Monospace";
	}