<!--
.. title: POJ 2334 Simple prefix compression C++版
.. slug: poj-2334
.. date: 2013-04-07T05:57:11+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2334](http://poj.org/problem?id=2334)


这个题，有人说是水题，其实不然，很有难度的。

介绍下题目，一组字符串，可以压缩，比如

>abc  
>atest  
>atext  

可以写为

>abc  
>1test  
>3xt  

这样说就容易理解了，就是把与上个字符串相同的部分直接用数字表示，来节约位置，问压缩后用多少字符数（尽管多位数不是一个数，但是储存算一个单位）

现开始理解错了题意，以为所有字符串公用同一个j，后来WA了好多次，才知道每一个j只与上一个字符串有关！

介绍下我的算法，定义b和c两个字符串，每次c为上一个，b为新输入的字符串，然后依次扫描。有一点我觉得比较有意思的,我原来代码是

	:::cpp
	for(j=0;j<strlen(b);j++)

这样写的话，每次循环都要计算一次长度，但其实长度没有变，这样提交都是600ms的，用g++还会超时，后来想了半天，知道为什么了修改后100msAC，这样的题给了我很大的启发，算法中每一步都是会影响到算法的好坏的，优化算法要从小处做起。

代码中很明显可以看出，每一行使用的字符数，为字符串长-相同的长度+1.

代码如下：
	:::cpp
	/*Problem: 2334		User: awq123
	**Memory: 240K		Time: 94MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		int t,i,j,temp,num=0;
		char b[256],c[256];
		scanf("%d",&t;);
		scanf("%s",c);
		num+=strlen(c);
		for(i=2;i<=t;i++)
		{
			scanf("%s",b);
			temp=strlen(b);
			for(j=0;j<temp;j++)
				if(b[j]!=c[j])
					break;
			num+=(strlen(b)-j+1);
			strcpy(c,b);
		}
		cout<<num<<endl;
	}