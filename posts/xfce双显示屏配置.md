<!--
.. title: xfce双显示屏配置
.. slug: xfce
.. date: 2013-04-07T09:36:58+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

最近一直用xfce，的确感觉到了相比gnome时的轻量，最近老感觉自己笔记本的显示面积小了。所以试了下双显示屏设置

xfce不像gnome shell中一样在设置里就可以轻易的修改两个屏幕的平铺，

首先我们打开显示设置，开始-->设置-->设置管理器-->显示，启用两个显示器
![xfce](http://i.stack.imgur.com/ayCTI.png)

然后打开终端输入

>xrandr

你会得到类似这样的输出结果

	::txt
	Screen 0: minimum 320 x 200, current 2806 x 900, maximum 2806 x 2806
	LVDS connected 1366x768+1440+0 (normal left inverted right x axis y axis) 309mm x 174mm
	   1366x768       60.1*+
	   1280x768       60.1 +
	   1280x720       60.1 +
	   1024x768       60.1 +
	   1024x600       60.1 +
	   800x600        60.1 +
	   800x480        60.1 +
	   720x480        60.1 +
	   640x480        60.1 +
	DFP1 disconnected (normal left inverted right x axis y axis)
	CRT2 connected 1440x900+0+0 (normal left inverted right x axis y axis) 410mm x 256mm
	   1366x768       59.9 +
	   1440x900       59.9*+
	   1280x1024      75.0     60.0  
	   1280x960       60.0  
	   1280x800       75.0     60.0  
	   1152x864       75.0     60.0  
	   1280x768       59.9  
	   1280x720       60.0  
	   1024x768       75.0     70.1     60.0  
	   1024x600       60.0  
	   800x600        72.2     75.0     70.0     60.3     56.2  
	   800x480        60.0  
	   720x480        60.0  
	   640x480        75.0     72.8     60.0  

这里可以看到自己的两个显示器的名称，分别在connected前面没，我的是LVDS和CRT2，这里记住这两个单词

最后我们在终端输入

>xrandr --output LVDS --left-of CRT2
[
请根据你的具体情况修改参数，这样你会发现，完美的平铺两个桌面了，

PS：这里如果你是长期使用两个显示器的人可以考虑添加一个启动项来实现开机自动双显示器平铺～