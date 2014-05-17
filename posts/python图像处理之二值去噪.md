<!--
.. title: python图像处理之二值去噪
.. slug: python-image0
.. date: 2013-04-07T09:56:28+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

好久没有写什么文章了，最近一直忙于学习各种知识，没有一个整体的知识体系也就没有贸然写文章，其实我想慢慢提高文章质量，话不多说，今天说说我验证码识别的第一步处理，也就是验证码的二值化和去噪点

我们先来看看一张简单的验证码，这张也是我一直在使用的一个例子（懒得找。。。）

![2](http://jovesky-wordpress.stor.sinaapp.com/uploads/2012/09/2.jpg)


下面我使用的python-image库简称PIL库，下面一个算法由一个网友提供：

	:::python
	from PIL import Image

	img = Image.open('tmp.jpg') # 读入图片
	img = img.convert("RGBA")

	pixdata = img.load()

	#二值化

	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
		if pixdata[x, y][0] < 90:
		    pixdata[x, y] = (0, 0, 0, 255)

	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
		if pixdata[x, y][1] < 136:
		    pixdata[x, y] = (0, 0, 0, 255)

	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
		if pixdata[x, y][2] > 0:
		    pixdata[x, y] = (255, 255, 255, 255)

	img.save("input-black.gif", "GIF")

	#放大图像 方便识别
	im_orig = Image.open('input-black.gif')
	big = im_orig.resize((1000, 500), Image.NEAREST)


处理后的图片为

![2](http://jovesky-wordpress.stor.sinaapp.com/uploads/2012/09/input-black.gif)

效果还不错

PS：最近烦恼软件界面的设计