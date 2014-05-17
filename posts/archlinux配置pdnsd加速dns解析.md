<!--
.. title: archlinux配置pdnsd加速dns解析
.. slug: archlinuxpdnsddns
.. date: 2013-04-07T09:53:56+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

一直觉得linux上网没有windows那么快，网上搜索了下，推介通过软件缓存dns解析数据从而加快dns解析，下面我选择了pdnsd来完成这艰巨的使命！

1:安装pdnsd

>sudo pacman -S pdnsd


2:配置默认配置文件

>sudo cp /etc/pdnsd.conf.sample /etc/pdnsd.conf

打开/etc/pdnsd.conf   

server段修改为

	:::bash
	server {
		label= "myisp";
		ip = 114.114.114.114, 8.8.8.8;  # Put your ISP's DNS-server address(es) here.
		timeout=4;         # Server timeout; this may be much shorter
		interval=30m;      # Check every 30 minutes.
		purge_cache=off;   # Keep stale cache entries in case the ISP's
	}

这里我用的国内的114dns，我个人感觉速度不错，解析网站走的国内线路，还不会被劫持！
还有一点可选

>query_method=tcp_only;<

这可以避免dns污染，不过如果你写的是google的dns也就没必要担心

global段修改为

>min_ttl=96h;  
>max_ttl=1w;  

这里配置的是dns缓存保存的时间!

3：开机启动服务
打开rc.conf在networkmanage后面添加pdnsd

PS：理论上这样就可以使用了，在配置网络的时候选则dns 127.0.0.1即可！
我使用过程中重启就无法解析，重新启动一次pdnsd就可以，不知道这个是不是特例，后再安装networkmanager-dispatcher-pdnsd解决的