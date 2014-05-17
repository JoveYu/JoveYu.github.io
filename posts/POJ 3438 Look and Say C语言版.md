<!--
.. title: POJ 3438 Look and Say C语言版
.. slug: poj-3438
.. date: 2013-04-07T08:28:24+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3438](http://poj.org/problem?id=3438)


题目是一种压缩算法，比如11111是5个1就写成51，222333是3个2和3个3写成3233。依次类推。利用计数记录下相连的数的个数，当不连续的时候输出，不过这个题我的方法，循环完后还要输出漏掉的一次！


代码如下：

	:::cpp
	/*Problem: 3438		User: awq123
	**Memory: 168K		Time: 204MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <cstring>
	#include <iostream>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int t;
		char d[1005];
		scanf("%d",&t;);
		while(t--)
		{
			scanf("%s",d);
			int i,c=1;
			int len=strlen(d);
			for(i=1;i<len;i++)
			{
				if(d[i]==d[i-1])
				{
					c++;
				}
				else
				{
					printf("%d%c",c,d[i-1]);
					c=1;
				}
			}
			printf("%d%cn",c,d[i-1]);
		}

	}