<!--
.. title: UBUNTU下双显示器设置 
.. slug: ubuntu-display
.. date: 2013-04-07T09:31:18+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

ubuntu（GNOME）现在已经能很好的处理双屏了，无论是克隆方式还是扩展方式！
但有时我们需要一个不同的管理器如awesome、fluxbox这类简单的窗口管理器中又如何设置成双显呢？其实也很容易－－xrandr就可以了！

1、了解设置的名称

直接运行xrandr（不带任何参数）就可以显示出当前的显示设备及设备的模式。如，笔记本会显示出LVDS和VGA。要留意LVDS及VGA的名称，如有的可能显示是LVDS1和VGA1！这就是显示设备的名称，下面会用到。

2、测试你的配置文件xorg.conf的内容是否支持多显！可以运行：

xrandr --output VGA --right-of LVDS --auto  
测试下你的系统关于显示设备是否正确，如果提示超出屏幕大小限制，一般是因为xorg.conf设置有问题，可以在Section "Screen"中添加一虚拟屏的设置（粗体部分）：  
Section "Screen"  
Identifier "Default Screen"  
Monitor "Configured Monitor"  
Device "Configured Video Device"  
SubSection "Display"  
Virtual 2560 1024  
EndSubSection  
EndSection  

注：2560 1024是因为一个屏是1280＊800（笔记本液晶），另一个是1280＊1024（液晶显示器），宽取二屏之和，高取二者中最大值。  
提示：有人说可以把此处设置的更大一些，不必根据当前的二个屏宽高，直接设到如4000x2000，这样以后外屏改变也不必重新设置xorg.conf的这段内容了，没试过所以这里仅仅提示一下！  

3、xrandr常用命令（这里的VGA与LVDS分别换成第1步中的设备名，如VGA1、LVDS1）：  
xrandr --output VGA --same-as LVDS --auto  
打开外接显示器(--auto:最高分辨率)，与笔记本液晶屏幕显示同样内容（克隆）  
xrandr --output VGA --same-as LVDS --mode 1280x1024  
打开外接显示器(分辨率为1280x1024)，与笔记本液晶屏幕显示同样内容（克隆）  
xrandr --output VGA --right-of LVDS --auto   
打开外接显示器(--auto:最高分辨率)，设置为右侧扩展屏幕  
xrandr --output VGA --off  
关闭外接显示器  
xrandr --output VGA --auto --output LVDS --off  
打开外接显示器，同时关闭笔记本液晶屏幕（只用外接显示器工作）  
xrandr --output VGA --off --output LVDS --auto  
关闭外接显示器，同时打开笔记本液晶屏幕 （只用笔记本液晶屏）  