<!--
.. title: 我的第一个python程序
.. slug: python
.. date: 2013-04-07T09:09:46+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

其实平常都要写hello world程序的，但是python的hello world纠一句话。。。。orz
所以我纠不写了，这个例子是《python核心编程》的一个例子，是一个文本创建器
输入文件名，若不重复，再输入每一行，最后以.结束

PS：我修改了下源代码，加入了行号显示的功能


	:::python
	#!/usr/bin/env python

	'makeTextFile.py -- create text file'

	import os
	ls=os.linesep

	#get filename
	while True:
		fname=raw_input('input file name:')
		if os.path.exists(fname):
			print "ERROR:'%s' already exists" %fname
		else:
			break

	#get file content (text) lines
	all=[]
	print "nEnter lines ('.' by itself to quit).n"

	#loop until user terminates input
	i=1
	while True:
		print i,
		entry =raw_input('>')
		if entry =='.':
			break
		else:
			all.append(entry)
		i+=1

	#writr lines to file with proper line-ending
	fobj=open(fname,'w')
	fobj.writelines(['%s%s' %(x,ls)for x in all])
	fobj.close()
	print 'DONE!'