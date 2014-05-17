<!--
.. title: sizeof和strlen对比
.. slug: sizeofstrlen
.. date: 2013-04-07T06:09:02+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

strlen()是用来求字符串长度的一个函数,sizeof()是用来求指定变量或者变量类型等所占内存大小的操作符。

这两个虽然都是量取长度的，但有本质的不同我们通过几个例子来看看！

	:::cpp
	char ss[]="0123456789";
	printf("%dn",sizeof(ss));
	printf("%dn",sizeof(*ss));

输出为

11    ss是数组，计算到''一共10+1  
1     *ss指第一个字符，所以为1  


	:::cpp
	char* ss="0123456789";
	printf("%dn",sizeof(ss));
	printf("%dn",sizeof(*ss));

输出

4     ss是指向字符串常量的字符指针，长整形的，所以为4    
1     *ss是第一个字符，为1  


	:::cpp
	char ss[100]="0123456789";
	printf("%dn",sizeof(ss));
	printf("%dn",strlen(ss));

输出

100     ss再内存中规定的大小就是100    
10      ss有10个字符，所以长度为10  

	:::cpp
	int ss[100]="0123456789";
	printf("%dn",sizeof(ss));
	printf("%dn",strlen(ss));

输出错误  

理论上第一个应该输出400     因为100长度再内存中占用100×4  
第二个错误  strlen后只能接字符指针